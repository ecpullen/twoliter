%global _cross_first_party 1
%undefine _debugsource_packages

Name: %{_cross_os}hello-log
Version: 0.0
Release: 0%{?dist}
Summary: Hello-log
License: Apache-2.0 OR MIT
URL: https://github.com/bottlerocket-os/bottlerocket

%description
%{summary}.

%prep
%setup -T -c
%cargo_prep

%build

%install
install -d %{buildroot}%{_cross_datadir}/logdog.d
echo "exec hello-logs echo Hello logs" > %{buildroot}%{_cross_datadir}/logdog.d/logdog.hello-log.conf

%files
%{_cross_datadir}/logdog.d/logdog.hello-log.conf
