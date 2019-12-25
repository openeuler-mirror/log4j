Name:           log4j
Version:        2.11.1
Release:        2
Summary:        Java logging package
BuildArch:      noarch
License:        ASL 2.0
URL:            http://logging.apache.org/log4j
Source0:        http://archive.apache.org/dist/logging/log4j/%{version}/apache-log4j-%{version}-src.tar.gz
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) maven-local mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin) mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin) mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.slf4j:slf4j-api) mvn(com.lmax:disruptor) mvn(org.jctools:jctools-core)
BuildRequires:  mvn(com.sun.mail:javax.mail) mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) mvn(org.slf4j:slf4j-ext)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml) mvn(sun.jdk:jconsole)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml) mvn(org.zeromq:jeromq)
BuildRequires:  mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec) mvn(org.slf4j:slf4j-ext)
BuildRequires:  mvn(com.datastax.cassandra:cassandra-driver-core) mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin) mvn(com.lmax:disruptor)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.eclipse.persistence:javax.persistence) mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.apache.logging:logging-parent:pom:) mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core) mvn(org.lightcouch:lightcouch)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin) mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.apache.commons:commons-compress) mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina) mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(commons-logging:commons-logging) mvn(javax.servlet:javax.servlet-api)
Obsoletes:      log4j-osgi < 2.9.1-4 log4j-liquibase < 2.9.1-4

%description
Apache Log4j 2 is an upgrade to Log4j that provides significant improvements over its predecessor,
Log4j 1.x, and provides many of the improvements available in Logback while fixing some inherent
problems in Logback’s architecture.

%package        slf4j
Summary:        Binding between LOG4J 2 API and SLF4J

%description    slf4j
Binding between LOG4J 2 API and SLF4J.

%package        osgi
Summary:        Apache Log4J Core OSGi Bundles

%description    osgi
Apache Log4J Core OSGi Bundles.

%package        taglib
Summary:        Apache Log4j Tag Library

%description    taglib
Apache Log4j Tag Library for Web Applications.

%package        jcl
Summary:        Apache Log4j Commons Logging Bridge

%description    jcl
Apache Log4j Commons Logging Bridge.

%package        jmx-gui
Summary:        Apache Log4j JMX GUI
Requires:       java-devel

%description    jmx-gui
JMX GUI provides a Swing-based client for remotely editing the log4j configuration
and remotely monitoring StatusLogger output. The JMX GUI can be run as a stand-alone
application or as a JConsole plug-in.

%package        web
Summary:        Apache Log4j Web

%description    web
Support for Log4j in a web servlet container.

%package        bom
Summary:        Apache Log4j BOM

%description    bom
Apache Log4j 2 Bill of Material

%package        nosql
Summary:        Apache Log4j NoSql

%description    nosql
Use NoSQL databases such as MongoDB and CouchDB to append log messages.

%package        help
Summary:        Documentation for log4j
Obsoletes:      log4j-manual < %{version} log4j-javadoc < %{version}-%{release}
Provides:       log4j-javadoc = %{version}-%{release}

%description    help
Documentation for log4j.

%prep
%autosetup -n apache-log4j-%{version}-src
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin -r :maven-doap-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
find -name "*.jar" -delete
find -name "*.class" -delete
rm -rf docs/api
%pom_disable_module log4j-samples
%pom_disable_module log4j-distribution
%pom_disable_module log4j-flume-ng
%pom_disable_module log4j-perf
%pom_disable_module log4j-api-java9
%pom_disable_module log4j-core-java9
%pom_remove_dep -r :log4j-api-java9
%pom_remove_dep -r :log4j-core-java9
%pom_remove_plugin -r :maven-dependency-plugin
find log4j-core/ -name DisruptorBlockingQueueFactory.java -delete
%pom_remove_dep -r com.conversantmedia:disruptor
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients
%pom_disable_module log4j-liquibase
%pom_disable_module log4j-slf4j18-impl
%pom_disable_module log4j-jdbc-dbcp2
%pom_disable_module log4j-mongodb2
%pom_disable_module log4j-mongodb3
%pom_remove_dep :jconsole log4j-jmx-gui
%pom_add_dep sun.jdk:jconsole log4j-jmx-gui
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_remove_plugin :apache-rat-plugin log4j-bom
%pom_remove_plugin :maven-failsafe-plugin
%mvn_alias :log4j-1.2-api log4j:log4j
%mvn_file ':{log4j-1.2-api}' log4j/@1 log4j
%mvn_package ':log4j-slf4j-impl' slf4j
%mvn_package ':log4j-to-slf4j' slf4j
%mvn_package ':log4j-taglib' taglib
%mvn_package ':log4j-jcl' jcl
%mvn_package ':log4j-jmx-gui' jmx-gui
%mvn_package ':log4j-web' web
%mvn_package ':log4j-bom' bom
%mvn_package ':log4j-cassandra' nosql
%mvn_package ':log4j-couchdb' nosql
%mvn_package :log4j-core-its __noinstall
%build
%mvn_build -f
%install
%mvn_install
%jpackage_script org.apache.logging.log4j.jmx.gui.ClientGUI '' '' log4j/log4j-jmx-gui:log4j/log4j-core log4j-jmx false

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%dir %{_javadir}/log4j

%files slf4j -f .mfiles-slf4j

%files taglib -f .mfiles-taglib

%files jcl -f .mfiles-jcl

%files web -f .mfiles-web

%files bom -f .mfiles-bom

%files nosql -f .mfiles-nosql

%files jmx-gui -f .mfiles-jmx-gui
%{_bindir}/log4j-jmx

%files help -f .mfiles-javadoc

%changelog
* Mon Dec 23 2019 Ling Yang <lingyang2@huawei.com> - 2.11.1-2
- Package init
