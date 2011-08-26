ImageRetriever
==============

Image retriver is a simple Django app to help you get the missing
image from the server when developping (for example when you get a
fresh database and don't want to download again the 3Gb of images
for the few images you miss since last sync).

Install
-------

If you're using buildout, just add 'imageretriever' to your list of
eggs.

If not, you can install the egg to your python setup using::

  easy_install imageretriever

You can also download the sources and add them to your local environment.


Using image retriever
---------------------

Start the django shell, then type::

  from imageretriever.utils import sync_images
  sync_images('http://localhost:8000/', 'http://example.com/')

It will list all image fields in the models and download them if they
are not on your local filesystem.

You can also specify the number of milliseconds between each image
download (to avoid being too agressive with the server) and if you
want more information::

  sync_images('http://localhost:8000/', 'http://example.com/', 100, True)

