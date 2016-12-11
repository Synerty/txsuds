# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
__version__ = '0.0.1'
__version__ = '0.0.1'
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

"""
Suds is a lightweight SOAP python client that provides a
service proxy for Web Services.
"""

from .compat import basestring, unicode

#
# Project properties
#

__version__ = '0.0.1'
__build__ = "IN 20160428"

#
# Exceptions
#


class MethodNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, "Method not found: '%s'" % name)


class PortNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, "Port not found: '%s'" % name)


class ServiceNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, "Service not found: '%s'" % name)


class TypeNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, "Type not found: '%s'" % tostr(name))


class BuildError(Exception):
    msg = \
        """
        An error occured while building a instance of (%s).  As a result
        the object you requested could not be constructed.  It is recommended
        that you construct the type manually using a Suds object.
        Please open a ticket with a description of this error.
        Reason: %s
        """

    def __init__(self, name, exception):
        Exception.__init__(self, BuildError.msg % (name, exception))


class SoapHeadersNotPermitted(Exception):
    msg = \
        """
        Method (%s) was invoked with SOAP headers.  The WSDL does not
        define SOAP headers for this method.  Retry without the soapheaders
        keyword argument.
        """

    def __init__(self, name):
        Exception.__init__(self, self.msg % name)


def smart_str(s, encoding='utf-8', errors='strict'):
    """
__version__ = '0.0.1'

    If strings_only is True, don't convert (some) non-string-like objects.

    from django
    """
    if not isinstance(s, basestring):
        try:
            return str(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                # An Exception subclass containing non-ASCII data that doesn't
                # know how to print itself properly. We shouldn't raise a
                # further exception.
                return ' '.join(smart_str(arg, encoding, errors) for arg in s)
            return unicode(s).encode(encoding, errors)
    elif isinstance(s, unicode):
        return s.encode(encoding, errors)
    elif s and encoding != 'utf-8':
        return s.decode('utf-8', errors).encode(encoding, errors)
    else:
        return s


class WebFault(Exception):
    def __init__(self, fault, document):
        if hasattr(fault, 'faultstring'):
            Exception.__init__(self, smart_str("Server raised fault: '%s'" % fault.faultstring))
        self.fault = fault
        self.document = document

#
# Logging
#


class Repr:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return repr(self.x)

#
# Utility
#


def tostr(object, encoding=None):
    """ get a unicode safe string representation of an object """
    if isinstance(object, basestring):
        if encoding is None:
            return object
        else:
            return object.encode(encoding)
    if isinstance(object, tuple):
        s = ['(']
        for item in object:
            if isinstance(item, basestring):
                s.append(item)
            else:
                s.append(tostr(item))
            s.append(', ')
        s.append(')')
        return ''.join(s)
    if isinstance(object, list):
        s = ['[']
        for item in object:
            if isinstance(item, basestring):
                s.append(item)
            else:
                s.append(tostr(item))
            s.append(', ')
        s.append(']')
        return ''.join(s)
    if isinstance(object, dict):
        s = ['{']
        for item in object.items():
            if isinstance(item[0], basestring):
                s.append(item[0])
            else:
                s.append(tostr(item[0]))
            s.append(' = ')
            if isinstance(item[1], basestring):
                s.append(item[1])
            else:
                s.append(tostr(item[1]))
            s.append(', ')
        s.append('}')
        return ''.join(s)
    try:
        return unicode(object)
    except:
        return str(object)


class null:
    """
    The I{null} object.
    Used to pass NULL for optional XML nodes.
    """
    pass

class Object(object):
    """
    The python 3 base Object
    """
    pass

def objid(obj):
    return obj.__class__.__name__ + ':' + hex(id(obj))


from .client import Client
