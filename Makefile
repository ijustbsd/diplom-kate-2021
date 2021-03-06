THEME = О функции Миттаг-Леффлера и её приложениях в теории дифференциальных уравнений в дробных производных
STUDENT = Е.С. Тарасова
DEGREE = д. ф.-м. н., проф.
DIRECTOR = М.И. Каменский

SED = "s/{{theme}}/${THEME}/; s/{{student}}/${STUDENT}/; s/{{degree}}/${DEGREE}/; s/{{director}}/${DIRECTOR}/"

all:
	# титульный лист
	sed -e ${SED} titlepage.fodt > tp-output.fodt
	libreoffice --headless --convert-to pdf tp-output.fodt

	# .tex
	pdflatex -shell-escape diplom.tex
	biber diplom
	pdflatex -shell-escape diplom.tex
	pdflatex -shell-escape diplom.tex
	mv diplom.pdf Тарасова.pdf
	evince Тарасова.pdf &

presentation:
	pdflatex presentation.tex
	pdflatex presentation.tex
	evince presentation.pdf &

clean:
	rm -f *.aux *.log *.out *.toc *.pdf *.bbl *.bcf *.blg *.xml *.nav *.snm
	rm -f images/*.pdf
	rm -f tp-output.*
