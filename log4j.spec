Name:                log4j
Version:             2.13.2
Release:             1
Summary:             Java logging package
License:             Apache-2.0
URL:                 http://logging.apache.org/%{name}
Source0:             http://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz
Patch1:              logging-log4j-Remove-unsupported-EventDataConverter.patch
BuildRequires:       fdupes maven-local mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:       mvn(com.fasterxml.jackson.core:jackson-databind) mvn(com.lmax:disruptor)
BuildRequires:       mvn(com.sun.mail:javax.mail) mvn(org.apache.commons:commons-compress)
BuildRequires:       mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:       mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:       mvn(org.fusesource.jansi:jansi) mvn(org.jctools:jctools-core)
BuildRequires:       mvn(org.osgi:osgi.core) mvn(org.slf4j:slf4j-api) mvn(org.slf4j:slf4j-ext)
Obsoletes:           log4j-mini < %{version}-%{release}
BuildArch:           noarch
BuildRequires:       mvn(com.datastax.cassandra:cassandra-driver-core)
BuildRequires:       mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:       mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:       mvn(com.fasterxml.woodstox:woodstox-core) mvn(commons-logging:commons-logging)
BuildRequires:       mvn(javax.servlet.jsp:jsp-api) mvn(javax.servlet:javax.servlet-api)
BuildRequires:       mvn(org.apache.commons:commons-csv) mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:       mvn(org.eclipse.jetty:jetty-util)
BuildRequires:       mvn(org.eclipse.persistence:javax.persistence)
BuildRequires:       mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:       mvn(org.lightcouch:lightcouch) mvn(org.zeromq:jeromq) mvn(sun.jdk:jconsole)
Requires:            javapackages-tools
%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package slf4j
Summary:             Binding between LOG4J 2 API and SLF4J
%description slf4j
Binding between LOG4J 2 API and SLF4J.

%package jcl
Summary:             Apache Log4j Commons Logging Bridge
%description jcl
Apache Log4j Commons Logging Bridge.

%package osgi
Summary:             Apache Log4J Core OSGi Bundles
%description osgi
Apache Log4J Core OSGi Bundles.

%package taglib
Summary:             Apache Log4j Tag Library
%description taglib
Apache Log4j Tag Library for Web Applications.

%package jmx-gui
Summary:             Apache Log4j JMX GUI
Requires:            java-devel
%description jmx-gui
Swing-based client for remotely editing the log4j configuration and remotely
monitoring StatusLogger output. Includes a JConsole plug-in.

%package web
Summary:             Apache Log4j Web
%description web
Support for Log4j in a web servlet container.

%package bom
Summary:             Apache Log4j BOM
%description bom
Apache Log4j 2 Bill of Material

%package nosql
Summary:             Apache Log4j NoSql
%description nosql
Use NoSQL databases such as MongoDB and CouchDB to append log messages.

%package        help
Summary:             API documentation for %{name}
Obsoletes:           %{name}-manual < %{version}
Provides:            log4j-javadoc = %{version}-%{release}

%description    help
Documentation for log4j.

%prep
%autosetup -n apache-log4j-%{version}-src -p1
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin -r :maven-doap-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
%pom_remove_plugin -r :revapi-maven-plugin
find -name "*.jar" -delete
find -name "*.class" -delete
rm -rf docs/api
%pom_disable_module %{name}-distribution
%pom_disable_module %{name}-samples
%pom_disable_module %{name}-flume-ng
%pom_disable_module %{name}-perf
%pom_disable_module %{name}-api-java9
%pom_disable_module %{name}-core-java9
%pom_remove_dep -r :%{name}-api-java9
%pom_remove_dep -r :%{name}-core-java9
%pom_remove_plugin -r :maven-dependency-plugin
find log4j-core/ -name DisruptorBlockingQueueFactory.java -delete
%pom_remove_dep -r com.conversantmedia:disruptor
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients
%pom_disable_module %{name}-liquibase
%pom_disable_module %{name}-slf4j18-impl
%pom_disable_module %{name}-jdbc-dbcp2
%pom_disable_module %{name}-mongodb2
%pom_disable_module %{name}-mongodb3
%pom_remove_dep :jconsole %{name}-jmx-gui
%pom_add_dep sun.jdk:jconsole %{name}-jmx-gui
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_remove_plugin :apache-rat-plugin %{name}-bom
%pom_remove_plugin :maven-failsafe-plugin
%pom_disable_module %{name}-iostreams
%pom_disable_module %{name}-jul
%pom_disable_module %{name}-core-its
%pom_disable_module %{name}-jpa
%pom_disable_module %{name}-appserver
%pom_disable_module %{name}-spring-cloud-config
%pom_disable_module %{name}-kubernetes
%pom_disable_module %{name}-jpl
%{mvn_alias} :%{name}-1.2-api %{name}:%{name}
%{mvn_file} ':{%{name}-1.2-api}' %{name}/@1 %{name}
%{mvn_package} ':%{name}-slf4j-impl' slf4j
%{mvn_package} ':%{name}-to-slf4j' slf4j
%{mvn_package} ':%{name}-taglib' taglib
%{mvn_package} ':%{name}-jcl' jcl
%{mvn_package} ':%{name}-jmx-gui' jmx-gui
%{mvn_package} ':%{name}-web' web
%{mvn_package} ':%{name}-bom' bom
%{mvn_package} ':%{name}-cassandra' nosql
%{mvn_package} ':%{name}-couchdb' nosql
%{mvn_package} :log4j-core-its __noinstall

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
%jpackage_script org.apache.logging.log4j.jmx.gui.ClientGUI '' '' %{name}/%{name}-jmx-gui:%{name}/%{name}-core %{name}-jmx false

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%dir %{_javadir}/%{name}

%files slf4j -f .mfiles-slf4j

%files taglib -f .mfiles-taglib

%files jcl -f .mfiles-jcl

%files web -f .mfiles-web

%files bom -f .mfiles-bom

%files nosql -f .mfiles-nosql

%files jmx-gui -f .mfiles-jmx-gui
%{_bindir}/%{name}-jmx

%files help -f .mfiles-javadoc
%license LICENSE.txt
%doc NOTICE.txt

%changelog
* Wed Oct 21 2020 wangyue <wanyue92@huawei.com> - 2.13.2-1
- Upgrade to 2.13.2 to fix CVE-2020-9488

* Mon Dec 23 2019 Ling Yang <lingyang2@huawei.com> - 2.11.1-2
- Package init
