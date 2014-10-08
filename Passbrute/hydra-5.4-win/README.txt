
				H Y D R A

		     (c) 2001-2006 by van Hauser / THC
 	              <vh@thc.org> http://www.thc.org


INTRODUCTION
------------
Number one of the biggest security holes are passwords, as every password
security study shows.
This tool is a proof of concept code, to give researchers and security
consultants the possiblity to show how easy it would be to gain unauthorized
access from remote to a system.
THIS TOOL IS FOR LEGAL PURPOSES ONLY!
FOR USING THIS TOOL COMMERCIALLY, SEE THE LICENCE FILE!

There are already several login hacker tools available, however none does
either support more than one protocol to attack or support parallized
connects.
Currently this tool supports:
 TELNET, FTP, HTTP-GET, HTTP-HEAD, HTTPS-GET, HTTP-HEAD, HTTP-PROXY,
 HTTP-PROXY-NTLM, HTTP-FORM-GET HTTP-FORM-POST, HTTPS-FORM-GET,
 HTTPS-FORM-POSTLDAP2, LADP3, SMB, SMBNT, MS-SQL, MYSQL, POSTGRES,
 POP3-NTLM, IMAP, IMAP-NTLM, NNTP, PCNFS, ICQ, SAP/R3, Cisco auth,
 Cisco enable, SMTP-AUTH, SMTP-AUTH-NTLM, SSH2, SNMP, CVS, Cisco AAA,
 REXEC, SOCKS5, VNC, POP3 and VMware-Auth.
However the module engine for new services is very easy so it won't take a
long time until even more services are supported.
Planned are: SSH v1, Oracle and more.
Your help in writing these modules is highly appreciated!! :-)


HOW TO COMPILE
--------------
Type "./configure" and then "make" and "make install".
If you have CYGWIN, you have to follow the instructions "./configure" prints
after running.
For PalmPilot, run "./configure-palm".
For ARM processor mobiles, run "./configure-arm".


SUPPORTED PLATFORMS
-------------------
All UNIX platforms (linux, *bsd, solaris, etc.)
Mac OS/X
Windows with Cygwin (both ipv4 and ipv6)
Mobile systems with ARM processors and Linux (e.g. Zaurus, iPaq)
PalmOS


HOW TO USE
----------
Type "./configure", followed by "make" to compile hydra and then
"./hydra -h" to see the command line options.
You make also type "make install" to install hydra to /usr/local/bin.
Note that NO login/password file is included. Generate them yourself.
For Linux users, a GTK gui is available, try "./xhydra"


SPECIAL OPTIONS FOR MODULES
---------------------------
Via the third command line parameter (TARGET SERVICE OPTIONAL) or the -m
commandline option, you can pass one option to a module.
Only some modules actually use this, a few require this.
Here is the complete list:

service module   optional parameter
==============   =================================================
http[s]-{head|get}
                 specifies the page to authentication at (REQUIRED)
                  Value can be "/secret" or "http://bla.com/foo/bar" or
                  "https://test.com:8080/members"
http-proxy       specifies the page to authentication at (OPTIONAL,
                  default is http://www.suse.com/)
http[s]-form-{get|post}
                 specifies the page and the parameters for the web form.
                 the keyword "^USER^" is replaced with the login and
                 ^PASS^ with the password.
                 syntax:   <url>:<form parameters>:<failure string>
                 e.g.: /login.php:user=^USER^&pass=^PASS^&mid=123:incorrect
smbnt            value [L,LH,D,DH,B,BH] (REQUIRED)
                  (L) Check local accounts, (D) Domain Accounts, (B) Either
                  (H) interpret passwords as NTLM hashes
ldap2, ldap3     specifies the DN (OPTIONAL, you can also specify the DN
                  as login with -l)
cisco-enable     specifies the logon password for the cisco device (OPTIONAL)
                 Note: if you have an AAA, use the -l option for the username
                 and the optional parameter for the password of the user.
sapr3            specifies the client id, a number between 0 and 99 (REQUIRED)
telnet           specified the string which is displayed after a successful
                  login (case insensitive), use if the default in the telnet
                  module produces too many false positives (OPTIONAL)
postgres         database name to attack (OPTIONAL, default is template1)

An example for how to use this with the www module to hand over the web page
to authenticate to:
  hydra -l jdoe -P /tmp/passlist www.attack.com http /members/
is the same like:
  hydra -m /members/ -l jdoe -P /tmp/passlist www.attack.com http
other example:
  hydra -m LH -l administrator -P sam.dump nt.microsoft.com smbnt
still other example:
  hydra -l gast -p gast -m 6 -s 3200 sapr3.sap.com sapr3
or
  hydra -l bla -p blubb ms.com telnet "welcome hacker"

RESTORING AN ABORTED/CRASHED SESSION
------------------------------------
When hydra is aborted with Control-C, killed or crashs, it leavs a
"hydra.restore" file behind which contains all necessary information to
restore the session. This session file is written every 5 minutes.
NOTE: if you are cracking parallel hosts (-M option), this feature doesnt
work, and is therefore disabled!
NOTE: the hydra.restore file can NOT be copied to a different platform (e.g.
from little indian to big indian, or from solaris to aix)


HOW TO SCAN/CRACK OVER A PROXY
------------------------------
The environment variable HYDRA_PROXY_HTTP defines the web proxy (this works
just for the http/www service!).
The following syntax is valid:
  HYDRA_PROXY_HTTP="http://123.45.67.89:8080/"
For all other services, use the HYDRA_PROXY_CONNECT variable to scan/crack
via a web proxy's CONNECT call. It uses the same syntax. eg:
  HYDRA_PROXY_CONNECT=proxy.anonymizer.com:8000
If you require authentication for the proxy, use the HYDRA_PROXY_AUTH
environment variable:
  HYDRA_PROXY_AUTH="the_login:the_password"


ADDITIONAL HINTS
----------------
* uniq your dictionary files! this can save you a lot of time :-)
    cat words.txt | sort | uniq > dictionary.txt
* if you know that the target is using a password policy (allowing users
  only to choose password with a minimum length of 6, containing a least one
  letter and one number, etc. use the tool pw-inspector which comes along
  with the hydra package to reduce the password list:
    cat dictionary.txt | pw-inspector -m 6 -c 2 -n > passlist.txt


OPTIONS YOU WILL NEVER SEE IN HYDRA
-----------------------------------
In this section I put feature request which I will never implement within
hydra - and why.
? feeding login/passwords from stdin (e.g. from john)
# This will not be implemented as it would not be possible to use with
  a) the restore functionality  and  b) multiple targets
  workarounds for b) would be possible however ugly hacks which would
  sometimes not work. As this feature will therefore will not fit the other
  standard functionality, you will never see it here.


SPEED
-----
through the parallizing feature, this password cracker tool can be very
fast, however it depends on the protocol. The fastest is generally POP3,
then FTP, then Telnet, and the least IMAP.
Experiment with the task option (-t) to speed thinks up! The higher - the
faster ;-) (but too high, and it disables the service)


STATISTICS
----------
Run against a SuSE Linux 7.2 on localhost with a "-C FILE" containing
295 entries (294 tries invalid logins, 1 valid). Every test was run three
times (only for "1 task" just once), and the average noted down.

			P A R A L L E L    T A S K S
SERVICE	1	4	8	16	32	50	64	100	128
------- --------------------------------------------------------------------
telnet	23:20	5:58	2:58	1:34	1:05	0:33	0:45*	0:25*	0:55*
ftp	45:54	11:51	5:54	3:06	1:25	0:58	0:46	0:29	0:32
pop3	92:10	27:16	13:56	6:42	2:55	1:57	1:24	1:14	0:50
imap	31:05	7:41	3:51	1:58	1:01	0:39	0:32	0:25	0:21

(*)
Note: telnet timings can be VERY different for 64 to 128 tasks! e.g. with
128 tasks, running four times resulted in timings between 28 and 97 seconds!
The reason for this is unknown...

guesses per task (rounded up):
	295	74	38	19	10	6	5	3	3

guesses possible per connect (depends on the server software and config):
	telnet	4
	ftp	6
	pop3	1
	imap	3


BUGS & FEATURES
---------------
Email me if you find bugs or if you have written a new module.
vh@thc.org

Type Bits/KeyID    Date       User ID
pub  2048/CDD6A571 1998/04/27 van Hauser / THC <vh@reptile.rug.ac.be>

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: 2.6.3i

mQENAzVE0A4AAAEIAOzKPhKBDFDyeTvMKQ1xx6781tEdIYgrkrsUEL6VoJ8H8CIU
SeXDuCVu3JlMKITD6nPMFJ/DT0iKHgnHUZGdCQEk/b1YHUYOcig1DPGsg3WeTX7L
XL1M4DwqDvPz5QUQ+U+VHuNOUzgxfcjhHsjJj2qorVZ/T5x4k3U960CMJ11eOVNC
meD/+c6a2FfLZJG0sJ/kIZ9HUkY/dvXDInOJaalQc1mYjkvfcPsSzas4ddiXiDyc
QcKX+HAXIdmT7bjq5+JS6yspnBvIZC55tB7ci2axTjwpkdzJBZIkCoBlWsDXNwyq
s70Lo3H9dcaNt4ubz5OMVIvJHFMCEtIGS83WpXEABRG0J3ZhbiBIYXVzZXIgLyBU
SEMgPHZoQHJlcHRpbGUucnVnLmFjLmJlPokAlQMFEDVE0D7Kb9wCOxiMfQEBvpAD
/3UCDgJs1CNg/zpLhRuUBlYsZ1kimb9cbB/ufL1I4lYM5WMyw+YfGN0p02oY4pVn
CQN6ca5OsqeXHWfn7LxBT3lXEPCckd+vb9LPPCzuDPS/zYnOkUXgUQdPo69B04dl
C9C1YXcZjplYso2q3NYnuc0lu7WVD0qT52snNUDkd19ciQEVAwUQNUTQDhLSBkvN
1qVxAQGRTwgA05OmurXHVByFcvDaBRMhX6pKbTiVKh8HdJa8IdvuqHOcYFZ2L+xZ
PAQy2WCqeakvss9Xn9I28/PQZ+6TmqWUmG0qgxe5MwkaXWxszKwRsQ8hH+bcppsZ
2/Q3BxSfPege4PPwFWsajnymsnmhdVvvrt69grzJDm+iMK0WR33+RvtgjUj+i22X
lpt5hLHufDatQzukMu4R84M1tbGnUCNF0wICrU4U503yCA4DT/1eMoDXI0BQXmM/
Ygk9bO2Icy+lw1WPodrWmg4TJhdIgxuYlNLIu6TyqDYxjA/c525cBbdqwoE+YvUI
o7CN/bJN0bKg1Y/BMTHEK3mpRLLWxVMRYw==
=MdzX
-----END PGP PUBLIC KEY BLOCK-----
