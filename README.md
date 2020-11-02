# AutoMT
Automatisasi Mikrotik

Untuk pengawasan mengajar mikrotik kelas XII TKJ

menggunakan python dan modul python-paramiko

Install pada debian base
<pre>apt install python-paramiko</pre>

# Penggunaan
<pre>
#python automt.py
 Default. Alamat ip akan membaca seluruh alamat yang ada di file semuaip.
#python automt.py withlog
 Membuat file log : python automt.py
#python automt.py ip {ipaddress}
 Menjalankan perintah pada satu host (ipaddress)
</pre>

# Perintah yang di proses
<pre>
perintah = """
/ system identity pr
/ ip addr pr
/ ip route pr
/ ip fi nat pr
/ ip dhcp-server pr
"""
</pre>
Silahkan diedit seperlunya
