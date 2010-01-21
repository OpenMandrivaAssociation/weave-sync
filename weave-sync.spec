%define name	    weave-sync
%define version     1.0
%define snapshot    6865b07629d7
%define release     %mkrel 0.20100121.1

%define _requires_exceptions pear(.*)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Firefox synchronisation service
License:	GPL
Group:		Networking/WWW
URL:		https://wiki.mozilla.org/Labs/Weave/Sync/1.0/Setup
Source0:    weaveserver-sync-%{snapshot}.tar.bz2
Source1:    weave.sql
Requires:	apache-mod_php
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Weave is a Mozilla Labs project to integrate web services into Firefox by
allowing users to securely share their data with other instances of their own
software, other users and 3rd parties. The Weave project includes a Firefox
add-on, a server component, and data sharing APIs.

The first service under the Weave umbrella is the synchronization service. The
Weave Sync 1.0 add-on lets you securely take your Firefox experience with you
to all your Firefox browsers. Mozilla operates a hosted server, and the source
code for the server is open so that any user may operate their own server if
they wish. The synchronization product keeps bookmarks, history, form data,
passwords, tabs, and user preferences, and provides an API to allow add-on
developers to synchronize their data as well.

%prep
%setup -q -n weaveserver-sync-%{snapshot}
cp %{SOURCE1} .

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr 1.0 %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_sysconfdir}
mv  %{buildroot}%{_datadir}/%{name}/1.0/default_constants.php.dist \
    %{buildroot}%{_sysconfdir}/%{name}.conf
pushd  %{buildroot}%{_datadir}/%{name}/1.0
ln -s ../../../..%{_sysconfdir}/%{name}.conf default_constants.php
popd

# apache configuration
install -d -m 755 %{buildroot}%{_webappconfdir}
cat > %{buildroot}%{_webappconfdir}/%{name}.conf <<EOF

Alias /weave/1.0 %{_datadir}/%{name}/1.0/index.php
Alias /weave %{_datadir}/%{name}

<Directory %{_datadir}/%{name}>
    Options Indexes FollowSymLinks
    Order allow,deny
    Allow from all
</Directory>
EOF

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201010
%_post_webapp
%endif

%postun
%if %mdkversion < 201010
%_postun_webapp
%endif

%files
%defattr(-,root,root)
%doc README weave.sql
%config(noreplace) %{_webappconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}

