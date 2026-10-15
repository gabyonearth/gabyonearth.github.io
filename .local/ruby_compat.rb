# Parche solo para compilar en local con Ruby moderno (Liquid 4 usa métodos removidos).
# GitHub Pages no usa este archivo.
class Object
  def tainted?; false; end
  def taint; self; end
  def untaint; self; end
end
