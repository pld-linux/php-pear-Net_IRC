%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       IRC
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - IRC Client Class
Summary(pl):	%{_class}_%{_subclass} - Klasa klienta IRC
Name:		php-pear-%{_pearname}
Version:	0.0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
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

%description -l pl
Eksperymentalna klasa IRC pasuj�ca zar�wno do aplikacji klienckich,
jak i bot�w. Zalety:
 - Nie-blokuj�cy socket
 - Wiadomo�ci serwera obs�ugiwane przez systemowy callback
 - Pe�ne wsparcie dla logowania
 - Pe�ne statystyki
 - Udokumentowane API oraz podr�cznik

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
