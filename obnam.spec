Summary:	Backup program
Name:		obnam
Version:	1.4
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://code.liw.fi/debian/pool/main/o/obnam/%{name}_%{version}.orig.tar.gz
# Source0-md5:	9e36d47f8e3a441abe9c37ee7051d3ee
Source1:	%{name}.conf
URL:		http://liw.fi/obnam
BuildRequires:	python-cliapp
BuildRequires:	python-devel
BuildRequires:	python-larch
BuildRequires:	python-paramiko
BuildRequires:	python-tracing
BuildRequires:	python-ttystatus
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-cliapp
Requires:	python-larch
Requires:	python-paramiko
Requires:	python-tracing
Requires:	python-ttystatus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A backup tool.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/log

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/obnam.conf
touch $RPM_BUILD_ROOT/var/log/obnam.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/obnam
%attr(755,root,root) %{_bindir}/obnam-benchmark
%attr(755,root,root) %{_bindir}/obnam-viewprof
%attr(755,root,root) %{py_sitedir}/obnamlib/_obnam.so
%dir %{py_sitedir}/obnamlib
%dir %{py_sitedir}/obnamlib/plugins
%{py_sitedir}/obnamlib/*.py*
%{py_sitedir}/obnamlib/plugins/*.py*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/obnam.conf
%attr(660,root,logs) %ghost /var/log/obnam.log
%{_mandir}/man1/obnam-benchmark.1*
%{_mandir}/man1/obnam-viewprof.1*
%{_mandir}/man1/obnam.1*

