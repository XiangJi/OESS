Summary: OESS Perl Libraries
Name: perl-OESS
Version: 1.2.5
Release: 1%{?dist}
License: APL 2.0
Group: Network
URL: http://globalnoc.iu.edu
Source0: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

BuildRequires: perl(Array::Utils)
BuildRequires: perl(Carp::Always)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Devel::Cover)
BuildRequires: perl(DBI), perl(DBD::mysql)
BuildRequires: perl(File::Path)
BuildRequires: perl(FindBin)
BuildRequires: perl(GRNOC::Config)
BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(Net::DBus)
BuildRequires: perl(Pod::Coverage)
BuildRequires: perl(TAP::Harness)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(XML::Simple)

Requires: perl
Requires: perl(AnyEvent)
Requires: perl(AnyEvent::Fork)
Requires: perl(Array::Utils)
Requires: perl(Class::Accessor)
Requires: perl(Data::Dumper)
Requires: perl(Data::UUID)
Requires: perl(DateTime)
Requires: perl(DBI), perl(DBD::mysql)
Requires: perl(English)
Requires: perl(Exporter)
Requires: perl(File::ShareDir)
Requires: perl(Getopt::Long)
Requires: perl(Graph::Directed)
Requires: perl(Graph::Undirected)
Requires: perl(GRNOC::Config)
Requires: perl(GRNOC::Log)                  >= 1.0.4
Requires: perl(GRNOC::RabbitMQ)             >= 1.1.1
Requires: perl(GRNOC::RabbitMQ::Client)
Requires: perl(GRNOC::RabbitMQ::Dispatcher)
Requires: perl(GRNOC::RabbitMQ::Method)
Requires: perl(GRNOC::WebService::Client)   >= 1.4.1
Requires: perl(GRNOC::WebService)           >= 1.2.9
Requires: perl(GRNOC::WebService::Regex)
Requires: perl(JSON)
Requires: perl(JSON::XS)
Requires: perl(List::Compare)
Requires: perl(List::MoreUtils)
Requires: perl(Log::Log4perl)
Requires: perl(MIME::Lite::TT::HTML)
Requires: perl(Net::DBus)
Requires: perl(Net::DBus::Exporter)
Requires: perl(Net::DBus::Object)
Requires: perl(Net::DBus::Reactor)
Requires: perl(Net::Netconf)                >= 1.4.1
Requires: perl(Net::Netconf::Manager)
Requires: perl(POSIX)
Requires: perl(Proc::Daemon)
Requires: perl(Proc::ProcessTable)
Requires: perl(RRDs)
Requires: perl(Set::Scalar)
Requires: perl(SOAP::Lite)
Requires: perl(Socket)
Requires: perl(Storable)
Requires: perl(Switch)
Requires: perl(Sys::Syslog)
Requires: perl(Template)
Requires: perl(Time::HiRes)
Requires: perl(URI::Escape)
Requires: perl(XML::Simple)
Requires: perl(XML::Writer)
Requires: perl(XML::LibXML::XPathContext)

Provides: perl-OESS-Circuit, perl-OESS-Database, perl-OESS-DBus, perl-OESS-Topology,perl-OESS-Measurement,perl-OESS-FlowRule
Obsoletes: perl-OESS-Circuit, perl-OESS-Database, perl-OESS-DBus, perl-OESS-Topology,perl-OESS-Measurement,perl-OESS-FlowRule

AutoReq: no

%description

%define docdir /usr/share/doc/%{name}-%{version}/
%define template_dir /usr/share/oess-core/

%prep
%setup -q

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
make

%check


%install
rm -rf $RPM_BUILD_ROOT
make pure_install
%__mkdir -p -m 0775 $RPM_BUILD_ROOT%{docdir}/share/upgrade
%__mkdir -p -m 0775 $RPM_BUILD_ROOT%{docdir}/share/mpls/templates/juniper/13.3R8/L2CCC
%__mkdir -p -m 0775 $RPM_BUILD_ROOT%{docdir}/share/mpls/templates/juniper/13.3R8/L2VPLS
%__mkdir -p -m 0775 $RPM_BUILD_ROOT%{docdir}/share/mpls/templates/juniper/13.3R8/L2VPN
%__mkdir -p -m 0775 $RPM_BUILD_ROOT%{template_dir}
%__install etc/notification_templates.tmpl $RPM_BUILD_ROOT/%{template_dir}/
%__install etc/notification_bulk.tmpl $RPM_BUILD_ROOT/%{template_dir}/
%__install etc/notification_bulk.tt.html $RPM_BUILD_ROOT/%{template_dir}/
%__install etc/notification.tt.html $RPM_BUILD_ROOT/%{template_dir}/
%__install share/nddi.sql $RPM_BUILD_ROOT/%{docdir}/share/
%__install share/upgrade/* $RPM_BUILD_ROOT/%{docdir}/share/upgrade/
%__install share/mpls/templates/juniper/13.3R8/L2CCC/* $RPM_BUILD_ROOT/%{docdir}/share/mpls/templates/juniper/13.3R8/L2CCC
%__install share/mpls/templates/juniper/13.3R8/L2VPLS/* $RPM_BUILD_ROOT/%{docdir}/share/mpls/templates/juniper/13.3R8/L2VPLS
%__install share/mpls/templates/juniper/13.3R8/L2VPN/* $RPM_BUILD_ROOT/%{docdir}/share/mpls/templates/juniper/13.3R8/L2VPN
# clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man3/OESS::Circuit.3pm.gz
%doc %{_mandir}/man3/OESS::Database.3pm.gz
%doc %{_mandir}/man3/OESS::DBus.3pm.gz
%doc %{_mandir}/man3/OESS::FlowRule.3pm.gz
%doc %{_mandir}/man3/OESS::FV.3pm.gz
%doc %{_mandir}/man3/OESS::FWDCTL::Master.3pm.gz
%doc %{_mandir}/man3/OESS::FWDCTL::Switch.3pm.gz
%doc %{_mandir}/man3/OESS::Measurement.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Device::Juniper::MX.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Device.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Discovery::Interface.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Discovery::ISIS.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Discovery::LSP.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Discovery::Paths.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Discovery.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::FWDCTL.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Switch.3pm.gz
%doc %{_mandir}/man3/OESS::MPLS::Topology.3pm.gz
%doc %{_mandir}/man3/OESS::Notification.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Constant.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Daemon.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::MessageQueue.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Processor.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Provisioning.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Query.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Reservation.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Server.3pm.gz
%doc %{_mandir}/man3/OESS::NSI::Utils.3pm.gz
%doc %{_mandir}/man3/OESS::RabbitMQ::Client.3pm.gz
%doc %{_mandir}/man3/OESS::RabbitMQ::Dispatcher.3pm.gz
%doc %{_mandir}/man3/OESS::Topology.3pm.gz
%doc %{_mandir}/man3/OESS::Traceroute.3pm.gz
%doc %{_mandir}/man3/OESS::Watchdog.3pm.gz
%doc %{_mandir}/man3/OESS::Webservice.3pm.gz
%{template_dir}/notification_templates.tmpl
%{template_dir}/notification_bulk.tmpl
%{template_dir}/notification_bulk.tt.html
%{template_dir}/notification.tt.html
%{perl_vendorlib}/OESS/Circuit.pm
%{perl_vendorlib}/OESS/Database.pm
%{perl_vendorlib}/OESS/DBus.pm
%{perl_vendorlib}/OESS/FlowRule.pm
%{perl_vendorlib}/OESS/FV.pm
%{perl_vendorlib}/OESS/FWDCTL/Master.pm
%{perl_vendorlib}/OESS/FWDCTL/Switch.pm
%{perl_vendorlib}/OESS/Measurement.pm
%{perl_vendorlib}/OESS/MPLS/Device/Juniper/MX.pm
%{perl_vendorlib}/OESS/MPLS/Device.pm
%{perl_vendorlib}/OESS/MPLS/Discovery/Interface.pm
%{perl_vendorlib}/OESS/MPLS/Discovery/ISIS.pm
%{perl_vendorlib}/OESS/MPLS/Discovery/LSP.pm
%{perl_vendorlib}/OESS/MPLS/Discovery/Paths.pm
%{perl_vendorlib}/OESS/MPLS/Discovery.pm
%{perl_vendorlib}/OESS/MPLS/FWDCTL.pm
%{perl_vendorlib}/OESS/MPLS/Switch.pm
%{perl_vendorlib}/OESS/MPLS/Topology.pm
%{perl_vendorlib}/OESS/Notification.pm
%{perl_vendorlib}/OESS/NSI/Constant.pm
%{perl_vendorlib}/OESS/NSI/Daemon.pm
%{perl_vendorlib}/OESS/NSI/MessageQueue.pm
%{perl_vendorlib}/OESS/NSI/Processor.pm
%{perl_vendorlib}/OESS/NSI/Provisioning.pm
%{perl_vendorlib}/OESS/NSI/Query.pm
%{perl_vendorlib}/OESS/NSI/Reservation.pm
%{perl_vendorlib}/OESS/NSI/Server.pm
%{perl_vendorlib}/OESS/NSI/Utils.pm
%{perl_vendorlib}/OESS/RabbitMQ/Client.pm
%{perl_vendorlib}/OESS/RabbitMQ/Dispatcher.pm
%{perl_vendorlib}/OESS/Topology.pm
%{perl_vendorlib}/OESS/Traceroute.pm
%{perl_vendorlib}/OESS/Watchdog.pm
%{perl_vendorlib}/OESS/Webservice.pm
%{docdir}/share/nddi.sql
%{docdir}/share/upgrade/*
%{docdir}/share/mpls/templates/juniper/13.3R8/L2CCC/*
%{docdir}/share/mpls/templates/juniper/13.3R8/L2VPLS/*
%{docdir}/share/mpls/templates/juniper/13.3R8/L2VPN/*

%changelog
* Thu Dec  5 2013 AJ Ragusa <aragusa@grnoc.iu.edu> - OESS Perl Libs
- Initial build.
