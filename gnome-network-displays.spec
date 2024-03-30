Name:           gnome-network-displays
Version:        0.92.1
Release:        1
Summary:        Stream the desktop to Wi-Fi Display capable devices

# The icon is licensed CC-BY-SA
License:        GPLv3+ and CC-BY-SA
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0:        https://download.gnome.org/sources/%{name}/0.90/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libnm) >= 1.15.1
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  firewalld

Requires: libnma
Requires: %{_lib}gstrtspserver1.0_0
Requires: gnome-desktop
Requires: gtk+3.0
Requires: hicolor-icon-theme
Requires: networkmanager-wifi
Requires: gstreamer1.0-pipewire

%description
GNOME Network Displays allows you to cast your desktop to a remote display.
Currently implemented is support for casting to Wi-Fi Display capable devices
(a.k.a. Miracast).

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --all-name --with-gnome

%post
%firewalld_reload

%postun
%firewalld_reload

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-network-displays
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.NetworkDisplays.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%{_metainfodir}/org.gnome.NetworkDisplays.appdata.xml
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml
