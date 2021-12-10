# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class Lvm1Error(Exception):
    """A custom core Lvm1 exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(Lvm1Error, self).__init__(message)


class Lvm1NotImplemented(Lvm1Error):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(Lvm1NotImplemented, self).__init__(message)


class Lvm1APIError(Lvm1Error):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Lvm1 API'
        else:
            message = 'Http response error from Lvm1 API. {0}'.format(message)

        super(Lvm1APIError, self).__init__(message)


class Lvm1ApiAuthError(Lvm1APIError):
    """A custom exception for API authentication errors"""
    pass


class Lvm1MissingDependency(Lvm1Error):
    """A custom exception for missing dependencies."""
    pass


class Lvm1Warning(Warning):
    """Base warning for Lvm1."""


class Lvm1UserWarning(UserWarning, Lvm1Warning):
    """The primary warning class."""
    pass


class Lvm1SkippedTestWarning(Lvm1UserWarning):
    """A warning for when a test is skipped."""
    pass


class Lvm1DeprecationWarning(Lvm1UserWarning):
    """A warning for deprecated features."""
    pass
