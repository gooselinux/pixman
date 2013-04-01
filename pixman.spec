%define gitdate 20070827
%define gitrev 8ff7213f39edc1b2b8b60d6b0cc5d5f14ca1928d

Name:           pixman
Version:        0.18.4
Release:        1%{?dist}.1
Summary:        Pixel manipulation library

Group:          System Environment/Libraries
License:        MIT
URL:            http://cgit.freedesktop.org/pixman/
# To make git snapshots:
# ./make-pixman-snapshot.sh %{?gitrev}
# if no revision specified, makes a new one from HEAD.
Source0:        http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source1:	make-pixman-snapshot.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# BuildRequires:  automake autoconf libtool pkgconfig

%description
Pixman is a pixel manipulation library for X and cairo.

%package devel
Summary: Pixel manipulation library development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development library for pixman.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libpixman-1*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
* Tue Oct 19 2010 Soren Sandmann <ssp@redhat.com> - 0.18.4-2-el6_1.1
- Use the recommended nvr scheme for z streams.

* Tue Oct 19 2010 Soren Sandmann <ssp@redhat.com> - 0.18.4-2
- Bump revision number.

* Tue Oct 19 2010 Soren Sandmann <ssp@redhat.com> - 0.18.4-1
- Rebase to 0.18.4

* Mon Feb 8 2010 Soren Sandmann <ssp@redhat.com> - 0.16.6-1
- Update to 0.16.6

* Tue Dec 15 2009 Soren Sandmann <ssp@redhat.com> - 0.16.4-2
- Remove assert patch

* Tue Dec 15 2009 Soren Sandmann <ssp@redhat.com> - 0.16.4-1
- Update to 0.16.4

* Fri Dec 11 2009 Soren Sandmann <ssp@redhat.com> - 0.16.2-2
- Add patch to disable asserts in stable releases.

* Mon Sep 28 2009 Soren Sandmann <ssp@redhat.com> - 0.16.2-1
- pixman 0.16.2

* Fri Aug 28 2009 Soren Sandmann <ssp@redhat.com> - 0.16.0-1
- pixman 0.16.0

* Mon Aug 11 2009 Soren Sandmann <ssp@redhat.com> - 0.15.20-1
- pixman 0.15.20

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.15.18-3
- Use bzipped upstream tarball.
- Fix URL.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 21 2009 Soren Sandmann <ssp@redhat.com> 0.15.18-1
- pixman 0.15.18

* Mon Jul 13 2009 Soren Sandmann <ssp@redhat.com> 0.15.16-1
- pixman 0.15.16

* Wed Jun 24 2009 Soren Sandmann <ssp@redhat.com> 0.15.14-1
- pixman 0.15.14

* Wed Jun 17 2009 Soren Sandmann <ssp@redhat.com> 0.15.12-1
- pixman 0.15.12

* Fri Jun 5 2009 Soren Sandmann <ssp@redhat.com> 0.15.10-1
- pixman 0.15.10

* Sat May 30 2009 Soren Sandmann <ssp@redhat.com> 0.15.8-1
- pixman 0.15.8

* Fri May 22 2009 Soren Sandmann <ssp@redhat.com> 0.15.6-2
- pixman 0.15.6

* Fri May 15 2009 Soren Sandmann <ssp@redhat.com> 0.15.4-1
- pixman 0.15.4

* Wed May 13 2009 Soren Sandmann <ssp@redhat.com> 0.15.2-3
- Remove patch to implement new clipping rules as it was completely broken.

* Tue May 12 2009 Soren Sandmann <ssp@redhat.com> 0.15.2-2
- Add patch to implement new clipping rules.

* Thu Apr 16 2009 Soren Sandmann <ssp@redhat.com> 0.15.2-1
- pixman 0.15.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 7 2009 Soren Sandmann <sandmann@redhat.com> 0.14.0-1
- pixman 0.14.0

* Tue Dec 16 2008 Adam Jackson <ajax@redhat.com> 0.13.2-1
- pixman 0.13.2

* Sun Dec 14 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.12.0-3
- Rebuild for pkgconfig provides

* Tue Nov 18 2008 Dan Williams <dcbw@redhat.com> 0.12.0-2
- Actually build with the altivec detection fix (rh #472000, #451831)

* Wed Sep 17 2008 Soren Sandmann <sandmann@redhat.com> 0.12.0-1
- Upgrade to 0.12.0. Drop stripes patch.

* Wed Sep 10 2008 Soren Sandmann <sandmann@redhat.com> 0.11.10-2
- Add patch to fix stripes in the Nautilus selection retangle.

* Sat Sep 6 2008 Soren Sandmann <sandmann@redhat.com> 0.11.10-1
- Upgrade to 0.11.10. Drop altivec patch.

* Thu Jul 17 2008 Soren Sandmann <sandmann@redhat.com> 0.11.8-1
- Upgrade to 0.11.8. Drop altivec patch.

* Wed Jun 25 2008 Soren Sandmann <sandmann@redhat.com> 0.11.6-1
- Upgrade to 0.11.6. Drop fix for leak.

* Tue Jun 17 2008 David Woodhouse <dwmw2@infradead.org> 0.11.4-3
- Fix Altivec detection breakage (#451831)

* Fri Jun 13 2008 Soren Sandmann <sandmann@redhat.com> 0.11.4-2
- Plug bad leak (cherrypicked from master)

* Mon Jun  9 2008 Soren Sandmann <sandmann@redhat.com> 0.11.4-1
- Update to 0.11.4

* Mon Jun  9 2008 Soren Sandmann <sandmann@redhat.com> 0.11.2-1
- Update to 0.11.2

* Thu Apr  3 2008 Soren Sandmann <sandmann@redhat.com> 0.10.0-1
- Update to 0.10.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.6-4
- Autorebuild for GCC 4.3

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.9.6-3
- Third time's the charm.

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.9.6-2
- Second try.

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.9.6-1
- Update to 0.9.6 release.

* Wed Sep 05 2007 Adam Jackson <ajax@redhat.com> 0.9.5-1
- Update to 0.9.5 release.

* Mon Aug 27 2007 Adam Jackson <ajax@redhat.com> 0.9.0-7.20070827
- New snapshot

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> 0.9.0-4.20070824
- New snapshot

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 0.9.0-3.20070724
- rebuild for toolchain bug

* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 0.9.0-2.20070724
- Re-add it, %%dir is not the same as adding a dir whole.

* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 0.9.0-1.20070724
- Remove redundant header from %%files devel.

* Fri May 18 2007 Adam Jackson <ajax@redhat.com> 0.9.0-0.20070724
- git build so I can build git X.
