<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
<body>
    <div>
        <h1 class="gap">
             0x01. NoSQL
        </h1>
    </div>
    <div id="project_id" style="display: none" data-project-id="1233"></div>
    <div class="panel panel-default" id="project-description">
        <div class="panel-body">
            <h2>Resources</h2>
            <p><strong>Read or watch</strong>:</p>
            <ul>
                <li><a href="/rltoken/wweK7dOY4pf8haCqv9Iv6Q" title="NoSQL Databases Explained" target="_blank">NoSQL Databases Explained</a> </li>
                <li><a href="/rltoken/QqqNmgzgwopHBv305ki6bg" title="What is NoSQL ?" target="_blank">What is NoSQL ?</a> </li>
                <li><a href="/rltoken/RyyP9OH1EMBWWYpTs4TqoA" title="MongoDB with Python Crash Course - Tutorial for Beginners" target="_blank">MongoDB with Python Crash Course - Tutorial for Beginners</a> </li>
                <li><a href="/rltoken/9__3tR-NimgXlmjPQwTF-Q" title="MongoDB Tutorial 2 : Insert, Update, Remove, Query" target="_blank">MongoDB Tutorial 2 : Insert, Update, Remove, Query</a> </li>
                <li><a href="/rltoken/ziEDeniRobC6owPE1_avAQ" title="Aggregation" target="_blank">Aggregation</a> </li>
                <li><a href="/rltoken/axwwF4CjO7FnK8Ecochqnw" title="Introduction to MongoDB and Python" target="_blank">Introduction to MongoDB and Python</a> </li>
                <li><a href="/rltoken/lUqnLwOHbbp9FK39ijNmDQ" title="mongo Shell Methods" target="_blank">mongo Shell Methods</a> </li>
                <li><a href="/rltoken/ZKAjSTq5ScfsUVhk_8DeFA" title="The mongo Shell" target="_blank">The mongo Shell</a> </li>
            </ul>
            <h2>Learning Objectives</h2>
            <p>By the end of this project you will be able to:</p>
             <ul> <u><h2>EXPLAIN THE FOLOWING</h2></u>
                <li>What NoSQL means</li>
                <li>What is difference between SQL and NoSQL</li>
                <li>What is ACID</li>
                <li>What is a document storage</li>
                <li>What are NoSQL types</li>
                <li>What are benefits of a NoSQL database</li>
                <li>How to query information from a NoSQL database</li>
                <li>How to insert/update/delete information from a NoSQL database</li>
                <li>How to use MongoDB</li>
            </ul>
        <h2>Requirements</h2>
        <h3>MongoDB Command File</h3>
        <ul>
            <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>MongoDB</code> (version 4.2)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be a comment: <code>// my comment</code></li>
            <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>The length of your files will be tested using <code>wc</code></li>
        </ul>
        <h3>Python Scripts</h3>
        <ul>
            <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7) and <code>PyMongo</code> (version 3.10)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
            <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the <code>pycodestyle</code> style (version 2.5.*)</li>
            <li>The length of your files will be tested using <code>wc</code></li>
            <li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
            <li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
            <li>Your code should not be executed when imported (by using <code>if __name__ == &quot;__main__&quot;</code>:)</li>
        </ul>
        <h2>More Info</h2>
        <h3>Install MongoDB 4.2 in Ubuntu 18.04</h3>
        <p><a href="/rltoken/8p4x14Ddn1UxKXZ5nPt3zA" title="Official installation guide" target="_blank">Official installation guide</a></p>
        <pre><code>$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
        $ echo &quot;deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse&quot; &gt; /etc/apt/sources.list.d/mongodb-org-4.2.list
        $ sudo apt-get update
        $ sudo apt-get install -y mongodb-org
        ...
        $  sudo service mongod status
        mongod start/running, process 3627
        $ mongo --version
        MongoDB shell version v4.2.8
        git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
        OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
        allocator: tcmalloc
        modules: none
        build environment:
            distmod: ubuntu1804
            distarch: x86_64
            target_arch: x86_64
        $  
        $ pip3 install pymongo
        $ python3
        &gt;&gt;&gt; import pymongo
        &gt;&gt;&gt; pymongo.__version__
        &#39;3.10.1&#39;
        </code></pre>
        <p>Potential issue if documents creation doesn&rsquo;t work or this error: <code>Data directory /data/db not found., terminating</code> (<a href="/rltoken/as8vd5VBnj4VDz5EINszMg" title="source" target="_blank">source</a> and <a href="/rltoken/9Df5v1NcWFFCn_sRNgsJUg" title="source" target="_blank">source</a>)</p>
        <pre><code>$ sudo mkdir -p /data/db
        </code></pre>
        <p>Or if <code>/etc/init.d/mongod</code> is missing, please find here an example of the file:</p>
        <details>
        <summary>Click to expand/hide file contents</summary>
    <pre><code>
        #!/bin/sh
        ### BEGIN INIT INFO
        # Provides:          mongod
        # Required-Start:    $network $local_fs $remote_fs
        # Required-Stop:     $network $local_fs $remote_fs
        # Should-Start:      $named
        # Should-Stop:
        # Default-Start:     2 3 4 5
        # Default-Stop:      0 1 6
        # Short-Description: An object/document-oriented database
        # Description:       MongoDB is a high-performance, open source, schema-free
        #                    document-oriented data store that's easy to deploy, manage
        #                    and use. It's network accessible, written in C++ and offers
        #                    the following features:
        #
        #                       * Collection oriented storage - easy storage of object- 
        #                         style data
        #                       * Full index support, including on inner objects
        #                       * Query profiling
        #                       * Replication and fail-over support
        #                       * Efficient storage of binary data including large
        #                         objects (e.g. videos)
        #                       * Automatic partitioning for cloud-level scalability
        #
        #                    High performance, scalability, and reasonable depth of
        #                    functionality are the goals for the project.
        ### END INIT INFO

        PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
        DAEMON=/usr/bin/mongod
        DESC=database

        NAME=mongod
        # Defaults.  Can be overridden by the /etc/default/$NAME
        # Other configuration options are located in $CONF file. See here for more:
        # http://dochub.mongodb.org/core/configurationoptions
        CONF=/etc/mongod.conf
        PIDFILE=/var/run/$NAME.pid
        ENABLE_MONGOD=yes

        # Include mongodb defaults if available.
        # All variables set before this point can be overridden by users, by
        # setting them directly in the defaults file. Use this to explicitly
        # override these values, at your own risk.
        if [ -f /etc/default/$NAME ] ; then
                . /etc/default/$NAME
        fi

        # Handle NUMA access to CPUs (SERVER-3574)
        # This verifies the existence of numactl as well as testing that the command works
        NUMACTL_ARGS="--interleave=all"
        if which numactl >/dev/null 2>/dev/null && numactl $NUMACTL_ARGS ls / >/dev/null 2>/dev/null
        then
            NUMACTL="`which numactl` -- $NUMACTL_ARGS"
            DAEMON_OPTS=${DAEMON_OPTS:-"--config $CONF"}
       
        DIETIME=10                  # Time to wait for the server to die, in seconds
                                    # If this value is set too low you might not
                                    # let some servers to die gracefully and
                                    # 'restart' will not work

        DAEMONUSER=${DAEMONUSER:-mongodb}
        DAEMONGROUP=${DAEMONGROUP:-mongodb}

        set -e
                else
                    NUMACTL=""
                    DAEMON_OPTS="-- "${DAEMON_OPTS:-"--config $CONF"}
                fi


                if test ! -x $DAEMON; then
                    echo "Could not find $DAEMON"
                    exit 0
                fi

                if test "x$ENABLE_MONGOD" != "xyes"; then
                    exit 0
                fi

                . /lib/lsb/init-functions

                STARTTIME=1
        running_pid() {
        # Check if a given process pid's cmdline matches a given name
            pid=$1
            name=$2
            [ -z "$pid" ] && return 1
            [ ! -d /proc/$pid ] &&  return 1
            cmd=`cat /proc/$pid/cmdline | tr "\000" "\n"|head -n 1 |cut -d : -f 1`
            # Is this the expected server
            [ "$cmd" != "$name" ] &&  return 1
            return 0
        }

        running() {
        # Check if the process is running looking at /proc
        # (works for all users)

            # No pidfile, probably no daemon present
            [ ! -f "$PIDFILE" ] && return 1
            pid=`cat $PIDFILE`
            running_pid $pid $DAEMON || return 1
            return 0
        }

        start_server() {
                    # Start the process using the wrapper
                    start-stop-daemon --background --start --quiet --pidfile $PIDFILE \
                                --make-pidfile --chuid $DAEMONUSER:$DAEMONGROUP \
                                --exec $NUMACTL $DAEMON $DAEMON_OPTS
                    errcode=$?
                return $errcode
        }

        stop_server() {
        # Stop the process using the wrapper
                    start-stop-daemon --stop --quiet --pidfile $PIDFILE \
                                --retry 300 \
                                --user $DAEMONUSER \
                                --exec $DAEMON
                    errcode=$?
                return $errcode
        }

        force_stop() {
        # Force the process to die killing it manually
                [ ! -e "$PIDFILE" ] && return
                if running ; then
                        kill -15 $pid
                # Is it really dead?
                        sleep "$DIETIME"s
                        if running ; then
                                kill -9 $pid
                                sleep "$DIETIME"s
                                if running ; then
                                        echo "Cannot kill $NAME (pid=$pid)!"
                                        exit 1
                                fi
                        fi
                fi
                rm -f $PIDFILE
        }


        case "$1" in
        start)
                log_daemon_msg "Starting $DESC" "$NAME"
                # Check if it's running first
                if running ;  then
                    log_progress_msg "apparently already running"
                    log_end_msg 0
                    exit 0
                fi
                if start_server ; then
                    # NOTE: Some servers might die some time after they start,
                    # this code will detect this issue if STARTTIME is set
                    # to a reasonable value
                    [ -n "$STARTTIME" ] && sleep $STARTTIME # Wait some time
                    if  running ;  then
                        # It's ok, the server started and is running
                        log_end_msg 0
                    else
                        # It is not running after we did start
                        log_end_msg 1
                    fi
                else
                    # Either we could not start it
                    log_end_msg 1
                fi
                ;;
        stop)
                log_daemon_msg "Stopping $DESC" "$NAME"
                if running ; then
                    # Only stop the server if we see it running
                                errcode=0
                    stop_server || errcode=$?
                    log_end_msg $errcode
                else
                    # If it's not running don't do anything
                    log_progress_msg "apparently not running"
                    log_end_msg 0
                    exit 0
                fi
                ;;
        force-stop)
                # First try to stop gracefully the program
                $0 stop
                if running; then
                    # If it's still running try to kill it more forcefully
                    log_daemon_msg "Stopping (force) $DESC" "$NAME"
                                errcode=0
                    force_stop || errcode=$?
                    log_end_msg $errcode
                fi
                ;;
        restart|force-reload)
                log_daemon_msg "Restarting $DESC" "$NAME"
                        errcode=0
                stop_server || errcode=$?
                # Wait some sensible amount, some server need this
                [ -n "$DIETIME" ] && sleep $DIETIME
                start_server || errcode=$?
                [ -n "$STARTTIME" ] && sleep $STARTTIME
                running || errcode=$?
                log_end_msg $errcode
                ;;
        status)

                log_daemon_msg "Checking status of $DESC" "$NAME"
                if running ;  then
                    log_progress_msg "running"
                    log_end_msg 0
                else
                    log_progress_msg "apparently not running"
                    log_end_msg 1
                    exit 1
                fi
                ;;
        # MongoDB can't reload its configuration.
        reload)
                log_warning_msg "Reloading $NAME daemon: not implemented, as the daemon"
                log_warning_msg "cannot re-read the config file (use restart)."
                ;;

        *)
                N=/etc/init.d/$NAME
                echo "Usage: $N {start|stop|force-stop|restart|force-reload|status}" >&2
                exit 1
                ;;
        esac

        exit 0
 </code></pre>
</details>
    <h3>Use &ldquo;container-on-demand&rdquo; to run MongoDB</h3>
    <ul>
    <li>Ask for container <code>Ubuntu 18.04 - MongoDB</code></li>
    <li>Connect via SSH</li>
    <li>Or via the WebTerminal</li>
    <li>In the container, you should start MongoDB before playing with it:</li>
    </ul>
    <pre><code>$ service mongod start
    * Starting database mongod                                              [ OK ]
    $
    $ cat 0-list_databases | mongo
    MongoDB shell version v4.2.8
    connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&amp;gssapiServiceName=mongodb
    Implicit session: session { &quot;id&quot; : UUID(&quot;70f14b38-6d0b-48e1-a9a4-0534bcf15301&quot;) }
    MongoDB server version: 4.2.8
    admin   0.000GB
    config  0.000GB
    local   0.000GB
    bye
    $
    </code></pre>

  </div>
</div>
    <h2 class="gap">TASKS: MANDATORY</h2>
    <div data-role="task11647" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11647">
  <span id="user_id" data-id="251885"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. List all databases
    </h3>
  </div>
    <p>Write a script that lists all databases in MongoDB.</p>
        </div>
</div>
    <h3>
      1. Create a database
    </h3>
    <!-- Task Body -->
    <p>Write a script that creates or uses the database <code>my_db</code>:</p>="task11649" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-11649">
  <span id="user_id" data-id="251885"></span>

  <div><h3>
      2. Insert document
    </h3>
        <!-- Task Body -->
    <p>Write a script that inserts a document in the collection <code>school</code>:</p>

<ul>
<li>The document must have one attribute <code>name</code> with value &ldquo;Holberton school&rdquo;</li>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>
 <div h3>
      3. All documents
    </h3>   
  </div>
     <!-- Task Body -->
    <p>Write a script that lists all documents in the collection <code>school</code>:</p>
<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
<
</div>
<h3>
      4. All matches
    </h3>


  <div class="panel-body">
    <span id="user_id" data-id="251885"></span>
    <!-- Task Body -->
    <p>Write a script that lists all documents with <code>name=&quot;Holberton school&quot;</code> in the collection <code>school</code>:</p>

<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>   
    <h3 >
      5. Count
    </h3>

  <!-- Task Body -->
    <p>Write a script that displays the number of documents in the collection <code>school</code>:</p>

<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>
<h1>NOTES</h1>
<h3> WHAT IS NOSQL</h3>
<li>stores unstractured data</li>
<li>example are databases like Redis, MongoDB, Cassandra</li>
<h3> TYPES OF NOSQL DATABASES</h3>
<ol>
    <li>Key-Value store</li>
    <p>data is partitioned and replicated across a cluster to get scalability and availability.<br>
    its highly effective in scaling application that has high velocity
    </p>
   <li> DOCUMENT STORES </li>
   <p> store self-describing <code>JASON, XML, BSON</code>documents</p></br>
   a value is a sinle document that stores all data related to a specific key</br>
   fields can be indexed to provide fast retrival without knowing the key</br>
   documents can have the same structure but have different values</br>
   </p>
   <li>WIDE COLUMN STORES </li>
   <p>store data in columns<br>
   name and formats of columns can vary from row to row<br>
   group columns of related data together<br>
   can retrieve related data in a single operation<br>
   </p>
   <li>GRAPH STORES</li>
   <p>store data as nodes and edges<br>
   store map and query relationships</br>
   adjacent elements are linked together without using index
   </pr>
</ol>
<h3>ADVANTAGES OF USING NOSQL</h3>
<ol>
    <li>SCALABILITY:</li>
    <p>use horizontal scale-out to make it is easy to add or reduce capacity as the need arises<br>
    </p>
    <li>PERFORMANCE:</li>
    <p> enables enterprices to continue delivering the best usre experience to their customers with a predictable return on investment for adding resources<br>
    </p>
 </ol>
<h1>AGGREGATION OPERATIONS</h1>
<ol>
    <li>SINGLE PURPOSE AGGREGATION METHOD</li>
    <p>aggregate data by a single purpose</p>
    <P>aggregation operations process  multiple docs and return computed resulrs.<br>
    can be used :<br>
    <ul><li>group values from multiple docs togther</li>
        <li>count the number of docs</li>
        <li>Perfom operations on the grouped data to return a single result</li>
        <li>Analtze data cjanges over time</li>
    </ul>
    <p>TO PERFORM AGGREGATION OPERATIONS:
    <ol>
        <li>AGGREGATION PIPELINES: </li>
        <li>Single pupose AGGREGATION METHODS</li>
    </ol>
</ol>
<h2>Aggregation Pipelines</h2>
consist of one or more stages that process documents:
<li>each stage performs an operation on the input documents and passes the result to the next stage example: <code> filter document, group document, calculative values</code></li>
<li>the documents that are output from a stage are passed to the next stage</li>
<li> aggregation pipeline can return results for groups of docs example <code>return the total</code>,<code>average</code>, <code>maximum</code>, <code>minimum</code> values</li>
<h3>AGGREGATION PIPELINES EXAMPLE</h3>
<p> aggregation pipeline with two stages and returns a total order quantity of medium size pizza grouped by pizza names</p>
<pre>
db.orders.aggregate( [

   // Stage 1: Filter pizza order documents by pizza size
   {
      $match: { size: "medium" }
   },

   // Stage 2: Group remaining documents by pizza name and calculate total quantity
   {
      $group: { _id: "$name", totalQuantity: { $sum: "$quantity" } }
   }

] )
</pre>
the <code>$match</code> stage:<br>
<li> is used to filter the documents by a condition.</li>
<li>filters the pizza order doc to pizza with a size of medium</li>
<li>passes the remaining documents to the <code>$group</code> stage</li>
the <code>$group</code> stage:<br>
<li>groups the remaining documents by puzza name </li>
<li>uses <code>$sum</code> to calulate the total order quantity for each pizza <code>name</code>.</li><br>
the total is stored in <code>totalQuantity</code> field returned by the aggregation pipeline

<h1>PYTHON AND MONGODB:</h1>
<h1>MONGO SHELL METHODS</code>

</body>
</html>