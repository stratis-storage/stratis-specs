## RPM specs for Stratis

* Get an account on [FAS](https://admin.fedoraproject.org/accounts/)
* Login and create a COPR project on http://copr.fedorainfracloud.org
* Install `fedora-packager`
* Download a given release from GitHub using `wget
  --content-disposition`. This is important to get the right filename
  for the .tar.gz.
* Update the spec for new version (`Version` field and add changelog entry)
* Run Mock to build srpm: `mock -r fedora-25-x86_64 --buildsrpm --spec
  <specname>.spec --sources . --resultdir=results`
* Run Mock to rebuild rpms: `mock -r fedora-25-x86_64 --rebuild
  results/<srpmname>.src.rpm --resultdir=results` Building locally first
  finds any errors more quickly than when COPR builds.
* COPR: Under Builds tab, create a new build
* Upload SRPM
