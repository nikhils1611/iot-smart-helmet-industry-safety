import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
import os
import requests
import seaborn as sns
import matplotlib.pyplot as plt

API_URL = "https://api.thingspeak.com/channels/2494591/feeds.json"

CHANNEL_ID = "2494591"

application = Flask(__name__)
application.secret_key = 'new'
application.config['MYSQL_HOST'] = 'localhost'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = 'admin'
application.config['MYSQL_DB'] = 'ehr_final'

mysql = MySQL(application)

application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = 'senduserdetails369@gmail.com'
application.config['MAIL_PASSWORD'] = 'kbzarexwcjdzdywv'
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
mail = Mail(application)

HOSTNAME = "ftp.drivehq.com"
FTP_PORT = '21'


# -----------------------------------    Admin routes --------------------------------------------


@application.route('/')
@application.route('/dataOwner_login', methods=['POST', 'GET'])
def dataOwner_login():
    if 'dataOwner_name' not in session:
        if request.method == 'POST':
            do_email = request.form["admin_id"]
            do_pwd = request.form["admin_pwd"]
            cur = mysql.connection.cursor()
            cur.execute("select * from m_dataowner where do_email=%s and do_password=%s", (do_email, do_pwd))
            user = cur.fetchone()
            if user:
                session['dataOwner_name'] = user[3]
                session['dataOwner_code'] = user[1]
                wish_msg = "Hello " + user[3]
                flash(wish_msg, 'success')
                return redirect(url_for('dataOwner_home'))
            else:
                msg = 'Invalid Login Details Try Again'
                return render_template('dataOwner/login.html', msg=msg)
        return render_template('dataOwner/login.html')
    return redirect(url_for('dataOwner_home'))


@application.route('/data_owner_list', methods=['POST', 'GET'])
def data_owner_list():
    if "dataOwner_name" in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM m_dataowner")
        data = cur.fetchall()
        return render_template('dataOwner/data_owner_list.html', data=data)
    return redirect(url_for('dataOwner_login'))


@application.route('/all_files_list', methods=['POST', 'GET'])
def all_files_list():
    if "admin" in session:
        cur = mysql.connection.cursor()
        # cur.execute("SELECT * FROM m_file_upload")
        cur.execute("SELECT f_no,date,do_name,du_code, f_name,f_remarks FROM m_file_upload, m_dataowner "
                    "WHERE m_file_upload.do_code=m_dataowner.do_code")
        data = cur.fetchall()
        return render_template('admin/all_files_list.html', data=data)
    return redirect(url_for('admin_login'))


@application.route('/all_users_list', methods=['POST', 'GET'])
def all_users_list():
    if "admin" in session:
        cur = mysql.connection.cursor()
        # cur.execute("SELECT * FROM m_data_user")
        cur.execute("SELECT * FROM m_data_user"
                    )
        data = cur.fetchall()
        return render_template('admin/all_users_list.html', data=data)
    return redirect(url_for('admin_login'))


@application.route('/create_dataOwner', methods=['POST', 'GET'])
def create_dataOwner():
    if "dataOwner_name" not in session:
        if request.method == 'POST':
            do_code = request.form['do_code']
            do_name = request.form['name']
            do_email = request.form['email']
            # do_phone = request.form['mobile']
            do_password = request.form['password']
            # algorithm_name = request.form['algorithm']

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT do_code FROM m_dataowner WHERE do_code=%s", (do_code,))
            d_code = cursor.fetchone()
            if not d_code:
                cursor.execute("SELECT do_email FROM m_dataowner WHERE do_email=%s", (do_email,))
                d_owner = cursor.fetchone()
                if not d_owner:
                    # if algorithm_name == 'rsa':
                    #     enc_keys = get_keys()
                    #     encryption_key = enc_keys[0]
                    #     decryption_key = enc_keys[1]
                    # else:
                    #     enc_keys = generate_keys()
                    #     encryption_key = str(enc_keys[0])
                    #     decryption_key = str(enc_keys[0])

                    cursor.execute('INSERT INTO m_dataowner(do_code,do_password,do_name,do_email)'
                                   'VALUES(%s,%s,%s,%s)',
                                   (do_code, do_password, do_name, do_email))

                    mysql.connection.commit()
                    cursor.close()

                    with open('static/credentials.txt', 'w') as file:
                        file.write(
                            'Hello {}...\n You can use below Credentials to login into your account.\n\nYour id : {}\n'
                            'User mail id: {}\nPassword : {}\n\n*Note : Do not forget to change your password after '
                            'login. '.format(do_name, do_code, do_email, do_password))

                    try:
                        subject = 'Login Credentials'
                        msg = Message(subject, sender='smtp.gmail.com', recipients=[do_email])
                        msg.body = "Hello  " + do_name + "  You have been created as data owner.. Below file contains your credentials"
                        with application.open_resource("static/credentials.txt") as fp:
                            msg.attach("credentials.txt", "application/txt", fp.read())
                        mail.send(msg)
                    except Exception as e:
                        print(e)
                        print("Something went wrong")
                    flash("New Data Owner Created Successfully ...", 'success')
                    return redirect(url_for('data_owner_list'))
                msg2 = "This Email Id is already Registered"
                return render_template('dataOwner/create_data_owner.html', msg1=msg2)
            msg2 = "This Code is not available to use.. try another.."
            return render_template('dataOwner/create_data_owner.html', msg1=msg2)
        return render_template('dataOwner/create_data_owner.html')
    return redirect(url_for('dataOwner_login'))


@application.route('/edit_dataOwner', methods=['POST', 'GET'])
def edit_dataOwner():
    if "admin" in session:
        if request.method == 'POST':
            do_code = request.form['do_code']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM m_dataowner WHERE do_code=%s", (do_code,))
            data = cursor.fetchone()
            cursor.close()
            return render_template('admin/update_data_owner.html', data=data)
        return render_template('admin/update_data_owner.html')
    return redirect(url_for('admin_login'))


@application.route('/update_dataOwner', methods=['POST', 'GET'])
def update_dataOwner():
    if "admin" in session:
        if request.method == 'POST':
            do_id = request.form['do_id']
            do_code = request.form['do_id']
            do_name = request.form['do_name']
            do_email = request.form['do_email']

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT do_name, do_email FROM m_dataowner WHERE do_id=%s", (do_id,))
            data1 = cursor.fetchone()

            if do_name == data1[0] and do_email == data1[1]:
                flash("No changes detected ...", 'success')
                return redirect(url_for('data_owner_list'))
            elif do_name != data1[0] and do_email == data1[1]:
                cursor.execute("UPDATE m_dataowner SET do_name=%s WHERE do_id = %s", (do_name, do_id))
                mysql.connection.commit()
                cursor.close()
                flash("Name successfully updated  ...", 'success')
                return redirect(url_for('data_owner_list'))
            elif do_name != data1[0] and do_email != data1[1]:
                cursor.execute("SELECT do_email FROM m_dataowner WHERE do_email=%s", (do_email,))
                d_owner = cursor.fetchone()
                if not d_owner:
                    cursor.execute("UPDATE m_dataowner SET do_name=%s, do_email=%s WHERE do_id = %s",
                                   (do_name, do_email, do_id))
                    mysql.connection.commit()
                    cursor.close()
                    flash("Name and Email successfully updated  ...", 'success')
                    return redirect(url_for('data_owner_list'))
                msg = 'This Email Id is already Existed'
                data = [do_id, do_code, '', do_name, do_email]
                return render_template('admin/update_data_owner.html', msg1=msg, data=data)

            elif do_name == data1[0] and do_email != data1[1]:
                cursor.execute("SELECT do_email FROM m_dataowner WHERE do_email=%s", (do_email,))
                d_owner = cursor.fetchone()
                if not d_owner:
                    cursor.execute("UPDATE m_dataowner SET do_email=%s WHERE do_id = %s", (do_email, do_id))
                    mysql.connection.commit()
                    cursor.close()
                    flash("Email successfully updated  ...", 'success')
                    return redirect(url_for('data_owner_list'))
                msg = 'This Email Id is already Existed'
                data = [do_id, do_code, '', do_name, do_email]
                return render_template('admin/update_data_owner.html', msg1=msg, data=data)
            return redirect(url_for('data_owner_list'))
        return render_template('admin/update_data_owner.html')
    return redirect(url_for('admin_login'))


# -----------------------------------    Data Owner routes --------------------------------------------
@application.route('/dataOwner_home', methods=['POST', 'GET'])
def dataOwner_home():
    if 'dataOwner_name' in session:
        return render_template('dataOwner/home.html', dataOwner_name=session['dataOwner_name'])
    return render_template('dataOwner/login.html')


@application.route('/users_list', methods=['POST', 'GET'])
def users_list():
    if 'dataOwner_name' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT du_id,du_name,du_email,a_name,do_name FROM m_data_user, m_attribute, m_dataowner "
                    "WHERE m_data_user.du_attribute=m_attribute.a_code and m_dataowner.do_code=m_data_user.do_code and"
                    " m_data_user.do_code=%s", (session['dataOwner_code'],))
        data = cur.fetchall()
        return render_template('dataOwner/users_list.html', data=data, dataOwner_name=session['dataOwner_name'])
    return redirect(url_for('dataOwner_login'))


@application.route('/create_user_page', methods=['POST', 'GET'])
def create_user_page():
    # if 'dataOwner_name' in session:
    if "admin" in session:
        if request.method == 'POST':
            user_id = request.form['user_id']
            username = request.form['username']
            DOJ = request.form['date']
            Age = request.form['age']
            Gender = request.form['gender']
            email = request.form['email']
            Password = request.form['password']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT du_email FROM m_data_user WHERE du_email=%s", (email,))
            user = cursor.fetchone()
            if not user:
                # cursor.execute("SELECT do_decryption_key FROM m_dataowner WHERE do_code=%s", (session['dataOwner_code'],))
                # pri_key = cursor.fetchone()
                # key = pri_key[0]
                # key_length = len(key)
                # new_attribute = attribute.zfill(key_length)
                # result = [chr(ord(a) ^ ord(b)) for a, b in zip(key, new_attribute)]
                # access_key = '-'.join(result)
                # # qr_code = main(username, Password)
                # print("generated qrcode:", qr_code)
                cursor = mysql.connection.cursor()
                cursor.execute(
                    "INSERT INTO m_data_user (du_id, du_name,du_doj, du_age, du_gender, du_email,du_password,do_code,du_url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (user_id, username, DOJ, Age, Gender, email, Password, str(session['admin'])))
                mysql.connection.commit()
                cursor.close()

                qr_code_filename = f"{username}.png"
                qr_code_image_path = os.path.join(os.getcwd(), qr_code_filename)

                print("Generated QR code111:", qr_code_filename)

                # send_email_with_qr(username, email, qr_code_image_path, user_id, Password)

                #
                # with open('static/credentials.txt', 'w') as file:
                #     file.write('Hello {}...\n You can use below Credentials to login into your account.\n\n'
                #                'User mail id: {}\nPassword : {}\nURL : {}\n\n*Note : Do not forget to change your password after '
                #                'login. '.format(username, email, Password, qr_code))
                #
                # try:
                #     subject = 'User Login Credentials'
                #     msg = Message(subject, sender='smtp.gmail.com', recipients=[email])
                #     msg.body = "Hello  " + username + "  You have been created as user below file contains your credentials."
                #     with application.open_resource("static/credentials.txt") as fp:
                #         msg.attach("credentials.txt", "application/txt", fp.read())
                #     mail.send(msg)
                # except Exception as e:
                #     print("Something went wrong", e)
                flash("New User Successfully Created...", "success")
                return redirect(url_for('all_users_list'))
            msg2 = "This Email Id is already Registered"
            return render_template('admin/create_user_page.html', msg1=msg2, admin=session['admin'])
        return render_template('admin/create_user_page.html', admin=session['admin'])
    return redirect(url_for('all_users_list'))


# @application.route('/generate_summary', methods=['POST'])
# def generate_summary():
#     uploaded_file = request.files['file']
#     summary = main1(uploaded_file)
#     return jsonify({'summary': summary})

@application.route('/dataOwner_files_list', methods=['POST', 'GET'])
def dataOwner_files_list():
    if 'dataOwner_name' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM m_file_upload WHERE do_code=%s", (session['dataOwner_code'],))
        data = cur.fetchall()
        return render_template('dataOwner/user_files_list.html', data=data, dataOwner_name=session['dataOwner_name'])
    return redirect(url_for('dataOwner_login'))


@application.route('/thinspeakdata', methods=['POST', 'GET'])
def thinspeakdata():
    hb_data = fetch_data_from_thingspeak(1)
    co_data = fetch_data_from_thingspeak(2)
    h_data = fetch_data_from_thingspeak(3)
    temp_data = fetch_data_from_thingspeak(4)

    line_graph1 = create_line_graph(hb_data, co_data, h_data, temp_data)
    print(line_graph1)

    return render_template('dataOwner/index.html', line_graph1=line_graph1, hb_data=hb_data, co_data=co_data, h_data=h_data,
                           temp_data=temp_data)


def create_line_graph(hb_data, co_data, h_data, temp_data):
    # Convert data to float
    hb_data = [float(hb) for hb in hb_data]
    co_data = [float(co) for co in co_data]
    h_data = [float(h) for h in h_data]
    temp_data = [float(temp) for temp in temp_data]


    # Find the minimum length among the data lists
    min_length = min(len(hb_data), len(co_data), len(h_data), len(temp_data))

    # Truncate or pad the lists to have the same length
    hb_data = hb_data[:min_length]
    co_data = co_data[:min_length]
    h_data = h_data[:min_length]
    temp_data = temp_data[:min_length]
    # Assuming Date and Time information is available with the fetched data
    dates = ['Data', 'Date2', 'Date3', 'Date4'][:min_length]  # Replace with your actual date information

    # Create a DataFrame using data
    df = pd.DataFrame({'Date and Time': dates, 'Heart Beat': hb_data, 'CO': co_data, 'Hum': h_data, 'Temp': temp_data})

    # Create a bar graph using Plotly
    fig = go.Figure()

    for column in df.columns[1:]:
        fig.add_trace(go.Bar(x=df['Date and Time'], y=df[column], name=column))

    # Update layout
    fig.update_layout(
        title='Bar Graph: Sensors data Values',
        xaxis_title='Sensed value names',
        yaxis_title=' Levels',
        legend=dict(
            title='Gas Type',
            orientation='h',
            yanchor='top',
            y=1.1,
            xanchor='right',
            x=1
        ),
        width=500,
        height=400,
        font=dict(size=13, color='white'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    graph_html = fig.to_html(full_html=False)
    return graph_html


def fetch_data_from_thingspeak(field_number):
    response = requests.get(API_URL.format(channel_id=CHANNEL_ID),
                            params={'results': 1, 'api_key': 'EILGGZRGLS1D787V'})
    if response.status_code == 200:
        data = response.json()
        feeds = data['feeds']
        field_data = [feed[f'field{field_number}'] for feed in feeds]
        print("field_data", field_data)
        return field_data
    else:
        return []


# @application.route('/dynamic_graph')
# def dynamic_graph():
#     # co_data = fetch_data_from_thingspeak(1)
#     # nh3_data = fetch_data_from_thingspeak(2)
#     # c6h6_data = fetch_data_from_thingspeak(3)
#     df = pd.read_excel('data.xlsx')
#     line_graph1 = line_graph(df)
#
#     return render_template('dataOwner/index.html', line_graph1=line_graph1)

@application.route('/users', methods=['POST', 'GET'])
def users():
    return render_template('dataOwner/users.html')


@application.route('/dataOwner_password_change', methods=['POST', 'GET'])
def dataOwner_password_change():
    if 'dataOwner_name' in session:
        if request.method == 'POST':
            current_pass = request.form['old']
            new_pass = request.form['new']
            verify_pass = request.form['verify']
            cur = mysql.connection.cursor()
            cur.execute("select do_password from m_dataowner WHERE do_code=%s", (session['dataOwner_code'],))
            user = cur.fetchone()
            if user:
                if user[0] == current_pass:
                    if new_pass == verify_pass:
                        msg = 'Password changed successfully'
                        cur.execute("UPDATE m_dataowner SET do_password=%s WHERE do_code=%s",
                                    (new_pass, session['dataOwner_code']))
                        mysql.connection.commit()
                        return render_template('dataOwner/dataOwner_password_change.html', msg1=msg,
                                               dataOwner_name=session['dataOwner_name'])
                    else:
                        msg = 'Re-entered password is not matched'
                        return render_template('dataOwner/dataOwner_password_change.html', msg2=msg,
                                               dataOwner_name=session['dataOwner_name'])
                else:
                    msg = 'Incorrect password'
                    return render_template('dataOwner/dataOwner_password_change.html', msg3=msg,
                                           dataOwner_name=session['dataOwner_name'])
            else:
                msg = 'Incorrect password'
                return render_template('dataOwner/dataOwner_password_change.html', msg3=msg,
                                       dataOwner_name=session['dataOwner_name'])
        return render_template('dataOwner/dataOwner_password_change.html',
                               dataOwner_name=session['dataOwner_name'])
    return redirect(url_for('dataOwner_login'))


@application.route('/dataOwner_profile', methods=['POST', 'GET'])
def dataOwner_profile():
    if 'dataOwner_name' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM m_dataowner WHERE do_code=%s ", (session['dataOwner_code'],))
        data = cursor.fetchone()
        cursor.close()
        return render_template('dataOwner/profile.html', data=data, dataOwner_name=session['dataOwner_name'])
    return redirect(url_for('dataOwner_login'))


@application.route('/dataOwner_logout')
def dataOwner_logout():
    if 'dataOwner_name' in session:
        do_name = session['dataOwner_name']
        session.pop('dataOwner_name')
        session.pop('dataOwner_code')
        msg = 'See you soon {}'.format(do_name)
        return render_template('dataOwner/login.html', msg=msg)
        # return redirect(url_for('dataOwner_login'))
    return redirect(url_for('dataOwner_login'))

if __name__ == '__main__':
    application.run(port=5001, debug=True)
