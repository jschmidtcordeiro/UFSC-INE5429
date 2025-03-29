# Makefile for LaTeX document compilation
# Author: João Pedro Schmidt Cordeiro

# Document name
DOCNAME = main

# Output directory
BUILDDIR = build

# LaTeX compiler and options
LATEX = pdflatex
LATEXFLAGS = -interaction=nonstopmode -file-line-error -output-directory=$(BUILDDIR)

# BibTeX compiler
BIBER = biber
BIBERFLAGS = --output-directory=$(BUILDDIR)

# Primary targets
all: pdf

pdf: $(DOCNAME).tex | $(BUILDDIR)
	@echo "===== Building $(DOCNAME).pdf ====="
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	$(BIBER) $(BIBERFLAGS) $(DOCNAME)
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	@cp $(BUILDDIR)/$(DOCNAME).pdf ./
	@echo "===== Build complete ====="

# Quick build without bibliography
quick: $(DOCNAME).tex | $(BUILDDIR)
	@echo "===== Quick building $(DOCNAME).pdf (no bibliography) ====="
	$(LATEX) $(LATEXFLAGS) $(DOCNAME)
	@cp $(BUILDDIR)/$(DOCNAME).pdf ./
	@echo "===== Quick build complete ====="

# Create build directory if it doesn't exist
$(BUILDDIR):
	mkdir -p $(BUILDDIR)

# Clean up temporary files
clean:
	@echo "===== Cleaning temporary files ====="
	rm -f $(BUILDDIR)/*.aux $(BUILDDIR)/*.log $(BUILDDIR)/*.out $(BUILDDIR)/*.toc $(BUILDDIR)/*.lof $(BUILDDIR)/*.lot 
	rm -f $(BUILDDIR)/*.idx $(BUILDDIR)/*.ind $(BUILDDIR)/*.ilg $(BUILDDIR)/*.bbl $(BUILDDIR)/*.blg 
	rm -f $(BUILDDIR)/*.bcf $(BUILDDIR)/*.run.xml $(BUILDDIR)/*.synctex.gz $(BUILDDIR)/*.fls $(BUILDDIR)/*.fdb_latexmk $(BUILDDIR)/*.mw
	@echo "===== Cleaning complete ====="

# Clean everything, including the generated PDF
cleanall: clean
	@echo "===== Removing PDF files ====="
	rm -f $(BUILDDIR)/$(DOCNAME).pdf
	rm -f $(DOCNAME).pdf
	@echo "===== Full cleaning complete ====="

# View the generated PDF
view: pdf
	open $(DOCNAME).pdf

# Declare phony targets
.PHONY: all pdf clean cleanall quick view 