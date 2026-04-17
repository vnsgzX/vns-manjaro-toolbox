# Maintainer: vnsgzx <https://github.com/vnsgzx>
pkgname=vns-manjaro-toolbox
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple and effective system maintenance tool for Manjaro Linux"
arch=('any')
url="https://github.com/vnsgzx/vns-manjaro-toolbox"
license=('GPL3')
depends=('python' 'python-pyqt6' 'pacman-mirrors')
source=("git+https://github.com/vnsgzx/vns-manjaro-toolbox.git")
md5sums=('SKIP')

package() {
  cd "$srcdir/$pkgname"
  
  # Pravimo foldere u sistemu
  install -d "$pkgdir/usr/bin"
  install -d "$pkgdir/usr/share/applications"
  
  # Kopiramo glavni program
  install -m755 main.py "$pkgdir/usr/bin/vns-manjaro-toolbox"
  
  # Kopiramo prečicu za meni
  install -m644 vns-manjaro-toolbox.desktop "$pkgdir/usr/share/applications/"
}
