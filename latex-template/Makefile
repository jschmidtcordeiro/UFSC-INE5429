# Makefile for LaTeX document compilation
# Author: João Pedro Schmidt Cordeiro

# Document name
DOCNAME = main

# LaTeX compiler and options
LATEX = pdflatex
LATEXFLAGS = -interaction=nonstopmode -file-line-error

# BibTeX compiler
BIBER = biber

# Primary targets
all: pdf

pdf: $(DOCNAME).tex
	@echo "===== Building $(DOCNAME).pdf ====="
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	$(BIBER) $(DOCNAME)
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	@echo "===== Build complete ====="

# Quick build without bibliography
quick: $(DOCNAME).tex
	@echo "===== Quick building $(DOCNAME).pdf (no bibliography) ====="
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	@echo "===== Quick build complete ====="

# Clean up temporary files
clean:
	@echo "===== Cleaning temporary files ====="
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.idx *.ind *.ilg
	rm -f *.bbl *.blg *.bcf *.run.xml *.synctex.gz *.fls *.fdb_latexmk *.mw
	rm -f $(DOCNAME).run.xml $(DOCNAME).bbl
	@echo "===== Cleaning complete ====="

# Clean everything, including the generated PDF
cleanall: clean
	@echo "===== Removing PDF file ====="
	rm -f $(DOCNAME).pdf
	@echo "===== Full cleaning complete ====="

# View the generated PDF
view: pdf
	open $(DOCNAME).pdf

# Declare phony targets
.PHONY: all pdf clean cleanall quick view 