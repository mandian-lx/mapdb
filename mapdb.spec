%{?_javapackages_macros:%_javapackages_macros}

Name:          mapdb
Version:       1.0.7
Release:       5%{?dist}
Summary:       Java database engine
License:       ASL 2.0
URL:           http://www.mapdb.org/
Source0:       https://github.com/jankotek/MapDB/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch


%description
MapDB provides concurrent Maps, Sets and
Queues backed by disk storage or off-heap
memory. It is a fast and easy to use
embedded Java database engine.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Cleanup
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :doxia-module-markdown
# lt.velykis.maven.skins:reflow-velocity-tools:1.0.0
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :site-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
# ch.raffael.pegdown-doclet:pegdown-doclet:1.1
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file : %{name}

%build

# Test fail @ random on arm builder
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 1.0.7-4
- add missing build requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 gil cattaneo <puntogil@libero.it> 1.0.7-1
- update to 1.0.7

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.0.6-3
- introduce license macro

* Mon Jan 19 2015 gil cattaneo <puntogil@libero.it> 1.0.6-2
- rebuilt for regenerate rpm {osgi,maven}.prov, {osgi,maven}.req

* Fri Jul 18 2014 gil cattaneo <puntogil@libero.it> 1.0.6-1
- update to 1.0.6

* Fri Jul 18 2014 gil cattaneo <puntogil@libero.it> 1.0.5-1
- initial rpm
