# Módulos customizados para Python (LINUX)
- Screenshot (Retorna uma imagem Pillow, para saber como manipular ver a documentação do Pillow);
# Dependencias:
* gi.repository;
	- *sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0*.
* Pillow;
	- *pip install pillow*.
	
# Como adicionar ao seu projeto:
Clone o repositorio com "git clone" na pasta de seu projeto, uma pasta chamada "custom_modules" irá aparecer, crie seu projeto um arquivo .py fora da pasta e, dentro desse arquivo, insira "*from custom_modules.MODULO import Função*". Para instalar o screenshot, por exemplo, insira "*from custom_modules.screenshot import ImageGrab*"
