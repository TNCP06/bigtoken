B

    [;�]�1  �            	   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZdZe�	d� e
e� edd�Ze �
e�Zej�ed �Zej�ed �Zej�� Zej�ed�Zd	eef Zd
ddd
dee� dd�Zejdeed�Zejdk�re� � Zed d Zdd� Zdd� Z dd� Z!ne
d� e�"�  y�eee� ej#dd
de dddd e d!�d"�� � Z$e$d# d$ Z%e%d%k�r�x:e&d&�e&d'�k �r�e e� e!e� �qnW ne
d(� e�"�  W n: e'k
�r�   e
d)� Y n e(k
�r�   e
d*� Y nX dS )+�    Nu�  

[36m  __ )  _)      __ __|       |           |   
  __ \   |   _` |  |   _ \   |  /   _ \  __| 
  |   |  |  (   |  |  (   |    <    __/  |   
 ____/  _| \__, | _| \___/  _|\_\ \___| \__| [1;30mbeta.
[36m           |___/                             
[31m[[37mAuthor: Akbar Neotech[31m]
[37m°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
�clearzcfg.json�r�emailZpasswordz%a, %d %b %Y %Xzpassword=%s&email=%szapi.bigtoken.comzapplication/jsonzPBIGtoken/1.1.0.4 Dalvik/2.1.0 Linux; U; Android 8.1.0; 524000d94bdb1754 Build/32z!application/x-www-form-urlencodedz%s�gzip)�Host�acceptz
user-agentzcontent-typezcontent-lengthzaccept-encodingzhttps://api.bigtoken.com/login)�url�data�headers��   �tokenZaccess_tokenc          	   C   s�   t jddd|  dddd�d��� }t jd	dd|  dddd
| d�d��� }|d d
 d |d d
 d  }td||d d |d d f � d S )Nz&https://api.bigtoken.com/users/profilezapi.bigtoken.comz	Bearer %szapplication/jsonzPBIGtoken/1.2.0.3 Dalvik/2.1.0 Linux; U; Android 8.1.0; 524000d94bdb1754 Build/38r   )r   �
authorizationr   z
user-agentzaccept-encoding)r   r
   z!https://api.bigtoken.com/users/mez%s GMT)r   r
   r   z
user-agentzaccept-encodingzif-modified-sincer	   �userZ
first_name�	last_namezX
[37mUsername [31m: [33m%s
[37mBalance  [31m: [33m%s
[37mRefferer [31m: [33m%s
Zavailable_big_points�referral_id)�requests�get�json�print)r   �waktusZi_openZi_opens�name� r   �plays.py�info!   s
    "( r   c             C   s�  t jddd|  ddddd�d	��� }tj|d
d�}t|�}t�d|�}t�d
|�}t�d|�}t�d|�}|d k�r&td� tt�d|���	dd��	dd��	dd�}|�	dd��
d�}	t|	d ��	dd��	dd�}
t�d|�}t|��	dd��	dd�}t|��	|
d��	dd��	dd��	dd��	dd��
d�}
t|��	|d��	dd��	dd��	dd��	dd��
d�}x�tt|��D ]�}|| }d|
| |d  || f }t j
d!|dd|  ddd"d#t|� d$d%�d&�}|�� }|jd'k�rtd(|d) d*  d+|d) d,  � t�d
� ntd-� td.� t�d/� �qpW n�td� x�tt|��D ]�}|| }d|| |d  || f }t j
d!|dd|  ddd"d#t|� d$d%�d&�}|�� }|jd'k�r�td(|d) d*  d+|d) d,  � t�d
� ntd-� td.� t�d/� �q<W d S )0Nz(https://api.bigtoken.com/users/dashboardzapi.bigtoken.comz	Bearer %szapplication/json�2zPBIGtoken/1.2.0.3 Dalvik/2.1.0 Linux; U; Android 8.1.0; 524000d94bdb1754 Build/38�deflate)r   r
   r   zx-srax-big-api-versionz
user-agentzaccept-encoding)r   r
   �   )�indentz"answer_type": "open_ended"z"data_point_key": "(.*?)"z?"option_uuid": "(.*?)",
                "mechanic": "question",z�{
                            "answer": "(.*?)",
                            "data_point_value": "(.*?)"
                        }
                    ]u�   [37m
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
|Mission Question|
↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
a   "option_uuid": "(.*?)",
                "mechanic": "question",
                "explanation": "(.*?)",
                "reward": (.*?),
                "content": {
                    "text": "(.*?)",
                    "label": "(.*?)",
                    "answer_type": "open_ended"z[(� �'z)]�"�,r   �[�]zJ"answer_type": "open_ended",
                    "data_point_key": "(.*?)"z '',z, z ,zR{"option_uuid":"%s","data_point_values":[{"values":["%s"],"data_point_key":"%s"}]}�   z'https://api.bigtoken.com/actions/submitzapplication/json; charset=utf-8z%sr   )r   r
   r   z
user-agentzcontent-typezcontent-lengthzaccept-encoding)r   r	   r
   r   z[32m�reward_data�msgu    [37m| [33m¢%s�reward_givenz[31mKlaim gagal!!!zs[31mCoba masuk akun BigToken anda lalu selesaikan beberapa misi di session tersebut secara manual terlebih dahulu.�   )r   r   r   �dumps�str�re�search�findallr   �replace�split�range�len�post�status_code�time�sleep)r   Zbuka�dumpZstr_dump�typ�keyZuuid�valueZhapusZhapussZ	hapus_uidZ	key_hapusZ	hapus_keyZuid�keys�i�valuesr	   �openZopens�x�vals�datasZopenrZopensrr   r   r   �question+   sR    $
(66,","rA   c       )      C   s�  t jddd|  ddddd�d	��� }tj|d
d�}t|�}t�d|�}t|�d
krptd� td� t	�
d� �ntd� �xtt|��D �]�}t jd||  dd|  dddd�d	�}|jdk�rXt|�� �}t�d|�}t|�d
k�r*t�d|�}	t�d|�}
t�d|�}|
d
 }d|d
 |d |	d
 f }
t
d|d
  d�}|�|
� |��  d}xVtt|	��D ]F}|
| }d|d |	| f }t
d|d
  d�}|�|� |��  �qbW t
d|d
  d��� }|d  }t jd!|dd|  ddd"d#t|� dd$�d%��� }td&|d' d(  d)|d' d*  � t	�
d+� �qztt�d,|���d-d.��d/d.��d0d.�}t|��|d.��d1d.��d/d.��d0d.��d-d.��d2�}�x@tt|��D �].}t jd||  dd|  dddd�d	�}t|�� �}t�d|�}t�d3|�}t|�d
k�r�t�d|�}t�d|�}t�d|�}|d
 }d|d
 |d |d
 f } t
d|d
  d�}!|!�| � |!��  d}"x`tt|��D ]F}"||" }#d|#d ||" f }$t
d|d
  d�}%|%�|$� |%��  �qrW ntd4� �q�W t|�d
k�r�nzt
d|d
  d��� }&|&d  }'t jd!|'dd|  ddd"d#t|'� dd$�d%��� }(td&|(d' d(  d)|(d' d*  � t	�
d+� q�td5� td6� t	�
d� t��  q�W d S )7Nz(https://api.bigtoken.com/users/dashboardzapi.bigtoken.comz	Bearer %szapplication/jsonr   zPBIGtoken/1.2.0.3 Dalvik/2.1.0 Linux; U; Android 8.1.0; 524000d94bdb1754 Build/38r   )r   r
   r   zx-srax-big-api-versionz
user-agentzaccept-encoding)r   r
   r   )r   z="option_uuid": "(.*?)",
                "mechanic": "survey",r   uy   [37m
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
|Mission Survey|
↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
z[31mMisi survey tidak ada.r(   z/https://api.bigtoken.com/actions?option_uuid=%sr   )r   r
   r   z
user-agentzaccept-encodingr   z*{'data': {'name': 'question_five_referral'z'data_point_key': '(.*?)',z2}, {'answer': '(.*?)', 'data_point_value': '(.*?)'z'option_uuid': '(.*?)'zP{"option_uuid":"%s","data_point_values":[{"values":["%s"],"data_point_key":"%s"}r$   �.�wz(,{"values":["%s"],"data_point_key":"%s"}za+r   z]}z'https://api.bigtoken.com/actions/submitzapplication/json; charset=utf-8z%s)r   r
   r   z
user-agentzcontent-typezcontent-lengthzaccept-encoding)r   r	   r
   z[32mr%   r&   u    [37m| [33m¢%sr'   �   z,'option_uuid': '(.*?)', 'mechanic': 'survey'r   r   r"   r#   z '',z, z	{'error':zL[31mSession error,selesaikan misi survey secara manual di session tersebut.z[31mSurvey gagal!!!zs[31mCoba masuk akun BigToken anda lalu selesaikan benerapa misi di session tersebut secara manual terlebih dahulu.)r   r   r   r)   r*   r+   r-   r1   r   r4   r5   r0   r3   r=   �write�close�readr2   r.   r/   �sys�exit))r   Zs_bukaZs_dumpZ
s_str_dumpZsurve�zZs_openZs_responZs_errorZs_keyZs_valueZs_uuidZs_valuesZs_data�opr>   r?   ZdatsZopsZhhr@   ZjalanZs_euidZs_edit�vZs_eopenZ	s_eresponZs_euuidZs_errorsZs_ekeyZs_evalueZ	s_evaluesZs_edataZs_op�qZs_evalsZs_datsrZs_opsrZs_hhZs_datasZs_jalanr   r   r   �survey^   s�    $&

0"(6&

0"
rN   z/[31mLogin gagal,periksa email & password Anda z&https://api.bigtoken.com/users/profilez	Bearer %szPBIGtoken/1.2.0.3 Dalvik/2.1.0 Linux; U; Android 8.1.0; 524000d94bdb1754 Build/38z%s GMT)r   r
   r   z
user-agentzaccept-encodingzif-modified-since)r   r
   r	   r   Z	EARNMOONEYr$   �   zV[31mGunakan kode reff [37m[ [33mEARNMOONEY [37m] [31muntuk menjalankan script ini.z
[31mKeluar program.....z:
[31mFile [37m'[33mcfg.json[37m' [31mtidak ditemukan.))r   r+   r   Zurllibr4   rH   Zdatetime�osZicon�systemr   r=   Zlogin�loadZcfg�parseZquoter   ZpasswdZnowZwaktuZstrftimer   �logr1   �headr2   Z	req_loginr3   Z
req_loginsr   r   rA   rN   rI   r   ZcekZceks�int�KeyboardInterrupt�FileNotFoundErrorr   r   r   r   �<module>   sN   @






3
W
(
