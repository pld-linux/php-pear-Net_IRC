%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       IRC
%define		_status		alpha

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - IRC Client Class
Summary(pl):	%{_pearname} - Klasa klienta IRC
Name:		php-pear-%{_pearname}
Version:	0.0.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	de6d4209e16de6e114f92cb7d803a7ab
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Experimental IRC Class suitable for both client or bots applications.
Features are:
 - Non-blocking sockets
 - Server messages handled by a callback system
 - Full logging capabilities
 - Full statistic collector
 - API Doc and Usage Manual

This class has in PEAR status: %{_status}.

%description -l pl
Eksperymentalna klasa IRC pasuj±ca zarówno do aplikacji klienckich,
jak i botów. Zalety:
 - Nie-blokuj±cy socket
 - Wiadomo¶ci serwera obs³ugiwane przez systemowy callback
 - Pe³ne wsparcie dla logowania
 - Pe³ne statystyki
 - Udokumentowane API oraz podrêcznik

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{doc/*,examples/*,tests/*}
%{php_pear_dir}/%{_class}/*.php
