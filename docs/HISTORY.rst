History
=======

0.4.2 (2014-11-03)
==================

* added subscriber and views for p.a.contenttypes
  [agitator]

* Upgrade mediaelement to 2.14.2
  [simahawk]

0.4.1 - 2013-07-18
==================

* Remove artifact from MEjs repository
  [afrepues]
* Depend on Plone-provided jQuery
  [afrepues]
* Match headings in the history with latest released version
  [afrepues]


0.4 - 2013-07-17
================

* Upgrade mediaelementjs library to 2.12.0 [mgogoulos]
* Refactor(view): add getContentType on view and not on context
  to make it easier to customize with dexterity [toutpt]

0.3 - 2013-05-15
================

* List all directly used packages as dependencies in setup.py
  [afrepues]
* Remove jquery from browser resource [toutpt]
* Update mediaelement to 2.11.2 [toutpt]
* Use link to display CSS stylesheet as it is the default in  Plone4 [toutpt]
* Add audio support [toutpt]
* Move audio and video init in ++resource++collective.mediaelement.js
  to support for all audio/video tags in the page. [toutpt]

0.2 - 2013-02-22
================

* Include the whole range of video formats supported by MEJS.
* Get initial size of Flash player from video metadata.
* Rewrite relative URLs in stylesheet when it is merged.
* Ignore file for git.
* Make sure all the needed files are packaged by distutils.

0.1.5 - 2012-06-28
==================

* upgraded mediaelement library to 2.9.1

0.1.4 - 2012-04-04
==================

* upgraded mediaelement library to 2.7.0

0.1.3 - 2011-12-08
==================

* Upgraded mediaelement library from 2.3.2 to 2.4.2

0.1.2 - 2011-11-26
==================

* Upgraded mediaelement library from 2.1.9 to 2.3.2

0.1.1 - 2011-08-19
==================

* Bugfix: remove (cargo-culted) resourceDirectory directives to non-existent
  directories that prevented startup of Zope (thanks to Kamon Ayeva for
  reporting this issue)

0.1 - 2011-08-19
================

* basic working version
