# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.mediaelementjs.interfaces import IMediaInfo, IAudio, IVideo
from Products.CMFPlone import __version__
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView

import os

PLONE5 = __version__ > '4.999'


class File(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.isVideo = None
        self.isAudio = None

    def __call__(self):
        # utility function to add resource to rendered page
        if PLONE5:
            add_resource_on_request(self.request, 'mediaelementjs')
        self.update()
        return self.index()

    def update(self):
        if self.isAudio is None:
            self.isAudio = IAudio.providedBy(self.context)
        if self.isVideo is None:
            self.isVideo = IVideo.providedBy(self.context)

    def video(self):
        if not self.isVideo:
            return
        info = IMediaInfo(self.context)
        return dict(
            url=self.href(),
            title=self.context.Title(),
            description=self.context.Description(),
            height=info.height,
            width=info.width,
            duration=info.duration
        )

    def audio(self):
        if not self.isAudio:
            return
        info = IMediaInfo(self.context)
        return dict(
            url=self.href(),
            title=self.context.Title(),
            description=self.context.Description(),
            duration=info.duration
        )

    def getFilename(self):
        context = aq_inner(self.context)
        return context.getFilename()

    def getContentType(self):
        return self.context.getContentType()

    def href(self):
        context = aq_inner(self.context)
        ext = ''
        url = context.absolute_url()
        filename = self.getFilename()
        if filename:
            extension = os.path.splitext(filename)[1]
            if not url.endswith(extension):
                ext = "?e=%s" % extension
        return self.context.absolute_url() + ext


class DXFile(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.isVideo = None
        self.isAudio = None

    def __call__(self):
        # utility function to add resource to rendered page
        if PLONE5:
            add_resource_on_request(self.request, 'mediaelementjs')
        self.update()
        return self.index()

    def update(self):
        if self.isAudio is None:
            self.isAudio = IAudio.providedBy(self.context)
        if self.isVideo is None:
            self.isVideo = IVideo.providedBy(self.context)

    def video(self):
        if not self.isVideo:
            return
        info = IMediaInfo(self.context)
        return dict(
            url=self.href(),
            title=self.context.Title(),
            description=self.context.Description(),
            height=info.height,
            width=info.width,
            duration=info.duration
        )

    def audio(self):
        if not self.isAudio:
            return
        info = IMediaInfo(self.context)
        return dict(
            url=self.href(),
            title=self.context.Title(),
            description=self.context.Description(),
            duration=info.duration
        )

    def filename(self):
        return self.context.file.filename

    def contentType(self):
        return self.context.file.contentType

    def href(self):
        context = aq_inner(self.context)
        ext = ''
        url = context.absolute_url()
        filename = self.filename()
        if filename:
            extension = os.path.splitext(filename)[1]
            if not url.endswith(extension):
                ext = "?e=%s" % extension
        return self.context.absolute_url() + ext
