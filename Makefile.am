ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}

SUBDIRS = .

# legacy rc script dir
rcdir=$(sysconfdir)/rc.d

# Inherit from systemd
pkgsysconfdir=$(sysconfdir)/systemd
systemconfigunitdir=$(pkgsysconfdir)/system
userconfigunitdir=$(pkgsysconfdir)/user
systemunitdir=$(rootprefix)/lib/systemd/system
userunitdir=$(prefix)/lib/systemd/user
udevlibexecdir=$(rootprefix)/lib/udev
udevhomedir=$(udevlibexecdir)
udevrulesdir=$(udevlibexecdir)/rules.d

# And these are the special ones for /
rootprefix=@rootprefix@
rootbindir=$(rootprefix)/bin
rootlibexecdir=$(rootprefix)/lib/systemd

if WITH_ENGMODE
engbindir=/opt/usr/devel/$(rootbindir)
endif

bin_SCRIPTS =
rc_SCRIPTS =
SCRIPT_IN_FILES =
sysconf_DATA =
systemconfigunit_DATA =
systemunit_DATA =
udevrules_DATA =

if WITH_ENGMODE
engbin_PROGRAMS =
endif

INSTALL_EXEC_HOOKS =
UNINSTALL_EXEC_HOOKS =

SHUTDOWN_TARGET_WANTS =
LOCAL_FS_TARGET_WANTS =
BASIC_TARGET_WANTS =
SYSINIT_TARGET_WANTS =
SOCKETS_TARGET_WANTS =
TIMERS_TARGET_WANTS =
TIZEN_INIT_TARGET_WANTS =
TIZEN_BOOT_TARGET_WANTS =
TIZEN_SYSTEM_TARGET_WANTS =
TIZEN_RUNTIME_TARGET_WANTS =
MULTI_USER_TARGET_WANTS =
DEFAULT_TARGET_WANTS =
SYSCONF_LOCAL_FS_TARGET_WANTS =

install-target-wants-hook:
	where=$(systemunitdir) && what="$(SHUTDOWN_TARGET_WANTS)" && wants=shutdown.target && $(add-wants)
	where=$(systemunitdir) && what="$(LOCAL_FS_TARGET_WANTS)" && wants=local-fs.target && $(add-wants)
	where=$(systemunitdir) && what="$(BASIC_TARGET_WANTS)" && wants=basic.target && $(add-wants)
	where=$(systemunitdir) && what="$(MULTI_USER_TARGET_WANTS)" && wants=multi-user.target && $(add-wants)
	where=$(systemunitdir) && what="$(SYSINIT_TARGET_WANTS)" && wants=sysinit.target && $(add-wants)
	where=$(systemunitdir) && what="$(SOCKETS_TARGET_WANTS)" && wants=sockets.target && $(add-wants)
	where=$(systemunitdir) && what="$(TIMERS_TARGET_WANTS)" && wants=timers.target && $(add-wants)
	where=$(systemunitdir) && what="$(SLICES_TARGET_WANTS)" && wants=slices.target && $(add-wants)
	where=$(systemunitdir) && what="$(TIZEN_INIT_TARGET_WANTS)" && wants=tizen-init.target && $(add-wants)
	where=$(systemunitdir) && what="$(TIZEN_BOOT_TARGET_WANTS)" && wants=tizen-boot.target && $(add-wants)
	where=$(systemunitdir) && what="$(TIZEN_SYSTEM_TARGET_WANTS)" && wants=tizen-system.target && $(add-wants)
	where=$(systemunitdir) && what="$(TIZEN_RUNTIME_TARGET_WANTS)" && wants=tizen-runtime.target && $(add-wants)
	where=$(systemunitdir) && what="$(TIZEN_RUNTIME_TARGET_WANTS)" && wants=tizen-runtime.target && $(add-wants)
	where=$(systemunitdir) && what="$(DEFAULT_TARGET_WANTS)" && wants=default.target && $(add-wants)
	where=$(systemconfigunitdir) && what="$(SYSCONF_LOCAL_FS_TARGET_WANTS)" && wants=local-fs.target && $(add-wants)

define add-wants
[ -z "$$what" -o -z "$$where" ] || ( \
	dir=$(DESTDIR)$$where/$$wants.wants && \
	$(MKDIR_P) -m 0755 $$dir && \
	cd $$dir && \
	rm -f $$what && \
	for i in $$what; do $(LN_S) ../$$i . || exit $$? ; done )
endef

INSTALL_EXEC_HOOKS += \
	install-target-wants-hook

bin_SCRIPTS += \
	scripts/cpu-governor.sh \
	scripts/resize2fs_by_partlabel.sh

sysconf_DATA += \
	conf/fstab

systemconfigunit_DATA += \
	units/opt.mount \
	units/opt-usr.mount \
	units/opt-system-csc.mount \
	units/csa.mount

if WITH_BOOT_PARTITION
systemconfigunit_DATA += \
	units/boot.mount
endif

systemunit_DATA += \
	units/usr-share-locale.mount \
	units/fsck@.service \
	units/resize2fs@.service \
	units/cpu-governor.service \
	units/resize2fs-root.service

LOCAL_FS_TARGET_WANTS += \
	usr-share-locale.mount \
	resize2fs-root.service

DEFAULT_TARGET_WANTS += \
	cpu-governor.service

SYSCONF_LOCAL_FS_TARGET_WANTS += \
	opt.mount \
	opt-usr.mount \
	opt-system-csc.mount \
	csa.mount

if WITH_BOOT_PARTITION
SYSCONF_LOCAL_FS_TARGET_WANTS += \
	boot.mount
endif

udevrules_DATA += \
	rules/51-tizen-system-plugin.rules

# ------------------------------------------------------------------------------
substitutions = \
       '|rootlibexecdir=$(rootlibexecdir)|' \
       '|rootbindir=$(rootbindir)|' \
       '|bindir=$(bindir)|' \
       '|SYSTEMCTL=$(rootbindir)/systemctl|' \
       '|SYSTEMD_NOTIFY=$(rootbindir)/systemd-notify|' \
       '|pkgsysconfdir=$(pkgsysconfdir)|' \
       '|SYSTEM_CONFIG_UNIT_PATH=$(pkgsysconfdir)/system|' \
       '|USER_CONFIG_UNIT_PATH=$(pkgsysconfdir)/user|' \
       '|pkgdatadir=$(pkgdatadir)|' \
       '|systemunitdir=$(systemunitdir)|' \
       '|userunitdir=$(userunitdir)|' \
       '|systempresetdir=$(systempresetdir)|' \
       '|userpresetdir=$(userpresetdir)|' \
       '|udevhwdbdir=$(udevhwdbdir)|' \
       '|udevrulesdir=$(udevrulesdir)|' \
       '|catalogdir=$(catalogdir)|' \
       '|tmpfilesdir=$(tmpfilesdir)|' \
       '|sysctldir=$(sysctldir)|' \
       '|PACKAGE_VERSION=$(PACKAGE_VERSION)|' \
       '|PACKAGE_NAME=$(PACKAGE_NAME)|' \
       '|PACKAGE_URL=$(PACKAGE_URL)|' \
       '|RANDOM_SEED=$(localstatedir)/lib/random-seed|' \
       '|prefix=$(prefix)|' \
       '|exec_prefix=$(exec_prefix)|' \
       '|libdir=$(libdir)|' \
       '|includedir=$(includedir)|' \
       '|VERSION=$(VERSION)|' \
       '|rootprefix=$(rootprefix)|' \
       '|udevlibexecdir=$(udevlibexecdir)|' \
       '|SUSHELL=$(SUSHELL)|' \
       '|DEBUGTTY=$(DEBUGTTY)|' \
       '|KILL=$(KILL)|' \
       '|KMOD=$(KMOD)|' \
       '|MKDIR_P=$(MKDIR_P)|' \
       '|QUOTAON=$(QUOTAON)|' \
       '|QUOTACHECK=$(QUOTACHECK)|' \
       '|SYSTEM_SYSVINIT_PATH=$(sysvinitdir)|' \
       '|VARLOGDIR=$(varlogdir)|' \
       '|RC_LOCAL_SCRIPT_PATH_START=$(RC_LOCAL_SCRIPT_PATH_START)|' \
       '|RC_LOCAL_SCRIPT_PATH_STOP=$(RC_LOCAL_SCRIPT_PATH_STOP)|' \
       '|PYTHON=$(PYTHON)|' \
       '|PYTHON_BINARY=$(PYTHON_BINARY)|' \
       '|INITAILBOOT_DONE=$(INITAILBOOT_DONE)|' \
       '|INITIALIZE_DONE=$(INITIALIZE_DONE)|' \
       '|READAHEAD_DIR=$(READAHEAD_DIR)|'

SED_PROCESS = \
	$(AM_V_GEN)$(MKDIR_P) $(dir $@) && \
	$(SED) $(subst '|,-e 's|@,$(subst =,\@|,$(subst |',|g',$(substitutions)))) \
		< $< > $@

units/%: units/%.in Makefile
	$(SED_PROCESS)

%.rules: %.rules.in Makefile
	$(SED_PROCESS)

%.sh: %.sh.in Makefile
	$(SED_PROCESS)
	$(AM_V_GEN)chmod +x $@

install-exec-hook: $(INSTALL_EXEC_HOOKS)
