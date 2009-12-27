# Functionality

huImages provides an infrastructure for storing, serving and scaling images.
It might not work for facebook or flickr scale image-pools, but for a few
hundred thousand images it woks very nicely. Currently it only supports
JPEG files.

When you upload an image, you get back a alpha-numeric ID back for further
accessing the image. You can get the URL of the Image via imageurl(ID) and
`scaled_imageurl(ID)`. You can get a complete XHTML `<img>` tag via
`scaled_tag(ID)`.

This module uses the concept of "sizes". A size can be a numeric specification
like "240x160". If the numeric specification ends with "!" (like in "75x75!")
the image is scaled and cropped to be EXACTLY of that size. IF not the image
keeps it aspect ratio.

You can use `get_random_imageid()`, `get_next_imageid(ID)` and
`get_previous_imageid(ID)` to implement image browsing.

# The image Server

`server.py` implements the image servin infrastructure. huImages assumes that
images are served form a separate server. We strongly suggest to serve them
from a separate domain. This domain should have which been used for cookies.
This is because the existence of cookies usually badly hurts caching
behaviour. "yourdomain-img.net" would be a good choice for a domain name. We
use "i.hdimg.net." for that purpose.

In the first few Versions of huImages Meta-Data and Images where stored in
[CouchDB][1]. After the fist few dozen Gigabytes it turned out that the huge
database files are a kind of headache and we moved to Storing the actual
original image data to [Amazon S3][2]. The server still is able to handle
Content stored in CouchDB and migrates it automatically to S3 where the need
arises.

[1]: http://couchdb.apache.org/
[2]: http://aws.amazon.com/s3

server.py works with any fast FastCGI compliant Webserver. It needs the
[Flup][3] toolkit installed to interface to a FastCGI enabled Server. We
use [lighttpd][4] for connectiong to it and `server.py` contains
configuration instructions for lighttpd. Of course you also can use other
httpd servers instead.

[3]: http://trac.saddi.com/flup
[4]: http://www.lighttpd.net/

server.py assumes that you have a filesystem which is able to handele very
large cache directories with no substential preformance penalty. We have been
running the system on [UFS2/dirhash][5] and XFS systems with success but it
should also work well on modenrn ext2/3 implementations with
[directory indexing][6].

[5]: http://code.google.com/soc/2008/freebsd/appinfo.html?csaid=69F96419FD4920FF
[6]: http://ext2.sourceforge.net/2005-ols/paper-html/node3.html

Wen a image is Requested and the original image is not in the Cache, the
original is pulled form CouchDB/S3 and put into the filesystem cache. Then the
[Python Imaging Library (PIL)[7] isused to generate the scaled version of the
image. The result is cached again in the filesystem and send to the client.

[7]: http://www.pythonware.com/products/pil/

If the image is requested again, it is served directly from the filesystem by
lighttpd without ever hitting the Python based `server.py`.

If you are short on diskspace fou can expire files from the cache directory
by just removint the oldest file until you have enough space again.



# Further Reading

 * http://blogs.23.nu/disLEXia/2009/02/imageserver/ (in german)
 * http://code.google.com/p/django-photologue/ (somewhat similar application)