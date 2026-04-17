# ... (početak fajla ostaje isti)
pkgname=vns-manjaro-toolbox
pkgver=1.0.1.r5.g828e27f  # Ovo će se automatski ažurirati
pkgrel=1
pkgdesc="My Manjaro Toolbox"
arch=('any')
url="https://github.com/vnsgzx/vns-manjaro-toolbox"
license=('GPL')
depends=('python-pyqt6')
makedepends=('git') # OBAVEZNO dodaj git ovde
source=("${pkgname}::git+${url}.git")
md5sums=('SKIP')

pkgver() {
  cd "$pkgname"
  # Generiše verziju u formatu: 1.0.1.r[broj_commitova].[hash_commita]
  printf "1.0.1.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$pkgname"
  # ... tvoj postojeći deo za instalaciju (install -Dm755...)
}
