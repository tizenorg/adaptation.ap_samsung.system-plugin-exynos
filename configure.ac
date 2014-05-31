#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.68])
AC_INIT(system-plugin-exynos, 0.1.01, [BUG-REPORT-ADDRESS])

AC_CONFIG_MACRO_DIR([m4])
AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE
AC_PREFIX_DEFAULT([/usr])
AM_INIT_AUTOMAKE([foreign])

# Checks for programs.
AC_PROG_MKDIR_P
AC_PROG_LN_S
AC_PROG_SED
AC_PROG_GREP
AC_PROG_AWK
#AC_PROG_INSTALL

# ------------------------------------------------------------------------------
AC_ARG_ENABLE([engmode],
        AS_HELP_STRING([--disable-engmode], [disable engineer mode]),
                [case "${enableval}" in
                        yes) with_engmode=yes ;;
                        no) with_engmode=no ;;
                        *) AC_MSG_ERROR(bad value ${enableval} for --disable-engmode) ;;
                esac],
                with_engmode=no)
AC_SUBST(WITH_ENGMODE)
AM_CONDITIONAL([WITH_ENGMODE], [test "x$with_engmode" != xno])

# ------------------------------------------------------------------------------
AC_ARG_ENABLE([xattr],
        AS_HELP_STRING([--disable-xattr],[Disable optional XATTR support]),
                [case "${enableval}" in
                        yes) have_xattr=yes ;;
                        no) have_xattr=no ;;
                        *) AC_MSG_ERROR(bad value ${enableval} for --disable-xattr) ;;
                esac],
                [have_xattr=auto])

if test "x${have_xattr}" != xno ; then
        AC_CHECK_HEADERS(
                [attr/xattr.h],
                [have_xattr=yes],
                [if test "x$have_xattr" = xyes ; then
                        AC_MSG_ERROR([*** XATTR headers not found.])
                fi])

        AC_CHECK_LIB(
                [attr],
                [fsetxattr],
                [have_xattr=yes],
                [if test "x$have_xattr" = xyes ; then
                        AC_MSG_ERROR([*** libattr not found.])
                fi])

        if test "x$have_xattr" = xyes ; then
                XATTR_LIBS="-lattr"
                AC_DEFINE(HAVE_XATTR, 1, [XATTR available])
        else
                have_xattr=no
        fi
else
        XATTR_LIBS=
fi
AC_SUBST(XATTR_LIBS)
AM_CONDITIONAL([HAVE_XATTR], [test "x$have_xattr" != xno])

# ------------------------------------------------------------------------------
AC_ARG_ENABLE([smack], AS_HELP_STRING([--disable-smack],[Disable optional SMACK support]),
                [case "${enableval}" in
                        yes) have_smack=yes ;;
                        no) have_smack=no ;;
                        *) AC_MSG_ERROR(bad value ${enableval} for --disable-smack) ;;
                esac],
                [have_smack=auto])

if test "x${have_xattr}" = xno; then
        if test "x${have_smack}" = xyes; then
                AC_MSG_ERROR(SMACK requires xattr support)
        else
                have_smack=no
        fi
else
        if test "x${have_smack}" = xauto; then
                have_smack=yes
        fi
fi

if test "x${have_smack}" = xyes ; then
        AC_DEFINE(HAVE_SMACK, 1, [Define if SMACK is available])
fi
# ------------------------------------------------------------------------------
AC_ARG_ENABLE([boot-partition],
        AS_HELP_STRING([--enable-boot-partition], [install boot partition units]),
                [case "${enableval}" in
                        yes) with_boot_part=yes ;;
                        no) with_boot_part=no ;;
                        *) AC_MSG_ERROR(bad value ${enableval} for --enable-boot-partition) ;;
                esac],
                with_boot_part=no)
AC_SUBST(WITH_BOOT_PARTITION)
AM_CONDITIONAL([WITH_BOOT_PARTITION], [test "x$with_boot_part" != xno])

# ------------------------------------------------------------------------------
AC_ARG_WITH([rootprefix],
        AS_HELP_STRING([--with-rootprefix=DIR],
                [rootfs directory prefix for config files and kernel modules]),
                [], [with_rootprefix=${ac_default_prefix}])
AC_SUBST([rootprefix], [$with_rootprefix])

# ------------------------------------------------------------------------------
AC_CONFIG_FILES([Makefile])

AC_OUTPUT
AC_MSG_RESULT([
        $PACKAGE_NAME $VERSION

        engineer mode:           ${with_engmode}

        XATTR:                   ${have_xattr}
        SMACK:                   ${have_smack}
        BOOT PARTITION:          ${with_boot_part}

        prefix:                  ${prefix}
        rootprefix:              ${with_rootprefix}
        sysconf dir:             ${sysconfdir}
        datarootdir:             ${datarootdir}
        lib dir:                 ${libdir}
])
