from Acquisition import aq_inner
import os

from Products.Five.browser import BrowserView

from collective.mediaelementjs.interfaces import IMediaInfo, IAudio, IVideo


class File(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.isVideo = None
        self.isAudio = None

    def __call__(self):
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
