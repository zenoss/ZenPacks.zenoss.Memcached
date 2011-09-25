# ZenPacks.zenoss.Memcached
This project is a [Zenoss][] extension (ZenPack) that allows for monitoring of
Memcached. See the Usage section for details on what is monitoring. This
ZenPack previously existed as a commercial-only extension to Zenoss called
ZenPacks.zenoss.MemcachedMonitor. Upon being released as open source its
name was changed to better match today's standards, and the version was reset
to 0.8.0 until it can be tested and verified by others.

There already exists a [very good community ZenPack][] for memcached by
[braudel][]. As far as I can see there is no compelling reason to use this
version over that. Ultimately I'd like to see the ZenPacks come together to
reduce confusion. At the time that this ZenPack was originally written, the
community version didn't exist.

## Dependencies
This ZenPack is known to be compatible with Zenoss versions 2.4 through 4.0.

## Installation
You must first have, or install, Zenoss 2.4.0 or later. Core and Enterprise
versions are supported. You can download the free Core version of Zenoss from
<http://community.zenoss.org/community/download>.

### Normal Installation (packaged egg)
Depending on what version of Zenoss you're running you will need a different
package. Download the appropriate package for your Zenoss version from the list
below.

 * Zenoss 4.1 - ???: Not yet available.
 * Zenoss 3.0 - 4.0: [Latest Package for Python 2.6][]
 * Zenoss 2.4 - 2.5: [Latest Package for Python 2.4][]

Then copy it to your Zenoss server and run the following commands as the zenoss
user.

    zenpack --install _<package.egg>_
    zenoss restart

### Developer Installation (link mode)
If you wish to further develop and possibly contribute back to the PostgreSQL
ZenPack you should clone the [git repository][], then install the ZenPack in
developer mode using the following commands.

    git clone git://github.com/zenoss/ZenPacks.zenoss.Memcached.git
    zenpack --link --install ZenPacks.zenoss.Memcached
    zenoss restart

## Usage
Installing the ZenPack will add a sample monitoring template called "memcached"
in the root of your device class tree. This makes it available to be bound to
any device in the system.

Assuming that you're running memcached on the standard port (11211/tcp), you
only need to go to the device class containing your memcached servers, or to
the individual device and bind the memcached template.

If you run memcached on a different port, you will either want to edit the
command template in the datasource within the memcached monitoring template to
change the port number.

The following graphs and their included metrics will be monitored on each
device the template is bound to.

 * memcached - CPU Utilization (rusage_system, rusage_user)
 * memcached - Memory Utilization (bytes, limit_maxbytes)
 * memcached - Cache Efficiency (get_hits, get_misses)
 * memcached - Requests (cmd_get, cmd_set, evictions)
 * memcached - Items Cached (curr_items, total_items)
 * memcached - Connections (curr_connections, total_connections, connection_structures)
 * memcached - Throughput (bytes_read, bytes_written)

## Screenshots
![CPU, Memory](https://github.com/zenoss/ZenPacks.zenoss.Memcached/raw/master/docs/memcached%20-%20Graphs%201.png)
![Efficiency, Requests, Items](https://github.com/zenoss/ZenPacks.zenoss.Memcached/raw/master/docs/memcached%20-%20Graphs%202.png)
![Connections, Throughput](https://github.com/zenoss/ZenPacks.zenoss.Memcached/raw/master/docs/memcached%20-%20Graphs%203.png)


[Zenoss]: <http://www.zenoss.com/>
[very good community ZenPack]: <http://community.zenoss.org/docs/DOC-5887>
[braudel]: <http://community.zenoss.org/people/braudel>
[Latest Package for Python 2.6]: <https://github.com/downloads/zenoss/ZenPacks.zenoss.Memcached/ZenPacks.zenoss.Memcached-0.8.0-py2.6.egg>
[Latest Package for Python 2.4]: <https://github.com/downloads/zenoss/ZenPacks.zenoss.Memcached/ZenPacks.zenoss.Memcached-0.8.0-py2.4.egg>
