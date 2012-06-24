Summary:	A C decompiler
Summary(pl):	Dekompilator C
Name:		uncc
Version:	0.1.2.1
Release:	2
License:	GPL
Group:		Development/Debuggers
Source0:	http://www.uncc.info/%{name}-%{version}.tar.gz
# Source0-md5:	57eeedd1c37a9046238f9967a4183603
URL:		http://www.uncc.info/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uncc is a C decompiler still. With this software the C source of a
program can be rebuilt (almost) automatically just having its already
compiled executable. The decompilation process is made with the
objdump disassembler. The uncc engine takes an assembly source file as
input and, through a series of recognition algorithms and expression
composition, it outputs a comparable C program out of it.

%description -l pl
uncc jest dekompilatorem C. Przy jego u�yciu mo�na (prawie)
automatycznie odtworzy� �r�d�a programu, do kt�rego mamy tylko ju�
skompilowany program wykonywalny. Proces dekompilacji jest wykonywany
przez disasembler objdump. Silnik uncc bierze �r�d�o asemblera z
wej�cia i poprzez szereg algorytm�w rozpoznawania i sk�adania wyra�e�
odtwarza por�wnywalny program w C.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D test/dasm.pl $RPM_BUILD_ROOT%{_bindir}/dasm.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* BUGS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
