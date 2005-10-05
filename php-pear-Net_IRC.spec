%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	IRC
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - IRC client class
Summary(pl):	%{_pearname} - klasa klienta IRC
Name:		php-pear-%{_pearname}
Version:	0.0.7
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5989ab3973044b0a330565b275667dc8
URL:		http://pear.php.net/package/Net_IRC/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

In PEAR status of this package is: %{_status}.

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
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{doc/*,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
