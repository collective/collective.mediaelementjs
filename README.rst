An integration of the MediaElementJS_ audio and video player
for Plone.

Large portions of this package have been blatantly copied from the
`collective.flowplayer`_ product by Martin Aspeli.

What it does
============

Once installed, supported media files uploaded to the Plone site will
automatically use a view that renders them with the MediaElementJS
player.

MediaElementJS uses ``<video>`` and ``<audio>`` tags on modern
browsers. If the browser doesn't support HTML5 media element tags, or
can not render the media natively, a Flash players that mimics the
`MediaElement API`_ is used. See the `MediaElementJS browser and
device support chart`_ for details.

The recognized formats at the moment are:

Audio
    MP3, Ogg, MPEG-4, WAV, Windows Media Audio, WebM

Video
    MPEG-4, Ogg, WebM, Flash Video, Windows Media Video, MPEG and QuickTime (``.mov`` and ``.qt``)

This package doesn't do any transcoding, if you need that have a look at wildcard.media

Installation
============

.. image:: https://secure.travis-ci.org/collective/collective.mediaelementjs.png
    :target: http://travis-ci.org/collective/collective.mediaelementjs

Follow the `quick instructions`_ in the Plone knowledge base.

.. _quick instructions: http://plone.org/documentation/kb/installing-add-ons-quick-how-to

Dependencies:

* hachoir_core
* hachoir_metadata
* hachoir_parser

Credits
=======

People
------

* `Tom Lazar <tom@tomster.org>`_ (author)
* `Servilio Afre Puentes <afrepues@mcmaster.ca>`_ (maintainer)
* `Markos Gogoulos <mgogoulos@unweb.me>`_
* `JeanMichel FRANCOIS <toutpt@gmail.com>`_
* `Peter Holzer <peter.holzer@agitator.com>`_

Companies
---------

* `Unweb.me <https://unweb.me/>`_
* `Makina-Corpus <http://www.makina-corpus.com>`_
* `McMaster University, Department of Family Medicine <http://fammed.mcmaster.ca/>`_


.. _MediaElementJS: http://mediaelementjs.com/
.. _collective.flowplayer: http://pypi.python.org/pypi/collective.flowplayer
.. _MediaElement API: http://www.w3.org/TR/html5/embedded-content-0.html#media-elements
.. _MediaElementJS browser and device support chart: http://mediaelementjs.com/#devices
