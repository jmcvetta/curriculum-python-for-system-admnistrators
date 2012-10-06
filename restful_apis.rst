************
RESTful APIs
************


What is a RESTful API?
======================

A 'RESTful API' is a remote API that follows the *REST* style of software
architecture.

REST - Representational State Transfer
--------------------------------------

REpresentational State Transfer (REST) is a style of software architecture for
distributed systems such as the World Wide Web. REST has emerged as a
predominant Web service design model. [#cit1]_

The term representational state transfer was introduced and defined in 2000 by
Roy Fielding in his doctoral dissertation. Fielding is one of the principal
authors of the Hypertext Transfer Protocol (HTTP) specification versions 1.0 and
1.1.

Conforming to the **REST constraints** is generally referred to as being
"RESTful".


The REST Constraints
--------------------

The REST architectural style describes the following six constraints applied to
the architecture, while leaving the implementation of the individual components
free to design: [#cit2]_


**Client–server**

A uniform interface separates clients from servers. This separation of concerns
means that, for example, clients are not concerned with data storage, which
remains internal to each server, so that the portability of client code is
improved. Servers are not concerned with the user interface or user state, so
that servers can be simpler and more scalable. Servers and clients may also be
replaced and developed independently, as long as the interface between them is
not altered.

**Stateless**

The client–server communication is further constrained by no client context
being stored on the server between requests. Each request from any client
contains all of the information necessary to service the request, and any
session state is held in the client.

**Cacheable**

As on the World Wide Web, clients can cache responses. Responses must therefore,
implicitly or explicitly, define themselves as cacheable, or not, to prevent
clients reusing stale or inappropriate data in response to further requests.
Well^managed caching partially or completely eliminates some client–server
interactions, further improving scalability and performance.

**Layered system**

A client cannot ordinarily tell whether it is connected directly to the end
server, or to an intermediary along the way. Intermediary servers may improve
system scalability by enabling load^balancing and by providing shared caches.
They may also enforce security policies.

**Code on demand** (optional)

Servers are able temporarily to extend or customize the functionality of a
client by the transfer of executable code. Examples of this may include compiled
components such as Java applets and client^side scripts such as JavaScript.

**Uniform interface**

The uniform interface between clients and servers, discussed below, simplifies
and decouples the architecture, which enables each part to evolve independently.
The four guiding principles of this interface are detailed below.

The only optional constraint of REST architecture is code on demand. If a
service violates any other constraint, it cannot strictly be considered RESTful.

Complying with these constraints, and thus conforming to the REST architectural
style enables any kind of distributed hypermedia system to have desirable
emergent properties, such as performance, scalability, simplicity,
modifiability, visibility, portability, and reliability.



JSON - Javascript Object Notation
---------------------------------

JSON, or *JavaScript Object Notation*, is a text-based open standard designed
for human-readable data interchange. It is derived from the JavaScript scripting
language for representing simple data structures and associative arrays, called
objects. Despite its relationship to JavaScript, it is language-independent,
with parsers available for many languages. [#cit3]_

The JSON format was originally specified by Douglas Crockford, and is described
in RFC 4627. The official Internet media type for JSON is ``application/json``. The
JSON filename extension is ``.json``.

The JSON format is often used for serializing and transmitting structured data
over a network connection. It is used primarily to transmit data between a
server and web application, serving as an alternative to XML.


Standard Library
================

.. todo::

   Describe use of standard library for REST API calls
   
   

*Requests* Libary
=================

.. todo::

   Describe use of *Requests* library for REST API calls



.. rubric:: Citations

.. [#cit1] http://en.wikipedia.org/wiki/Representational_state_transfer
.. [#cit2] http://en.wikipedia.org/wiki/Representational_state_transfer#Constraints
.. [#cit3] http://en.wikipedia.org/wiki/JSON