MAKE = make
PROGRAMS = mac2tac tac2mips tac-runner

.PHONY: $(PROGRAMS)

all: $(PROGRAMS)

mac2tac:
	cd src && $(MAKE) || \
	(echo -e "\n\033[1;31mError. \033[0mFrontend compilation termined." && exit 1)
	mv src/mac2tac bin/ 
	echo -e "\n\033[1;36mFrontend compilation successfully.\033[0m"

tac2mips:
	cd tools/translator && $(MAKE) || \
	(echo -e "\n\033[1;31mError. \033[0mTranslator compilation termined." && exit 1)
	mv tools/translator/tac2mips bin/ 
	echo -e "\n\033[1;36mTranslator compilation successfully.\033[0m"

tac-runner:
	cd tools/interpreter && $(MAKE) || \
	(echo -e "\n\033[1;31mError. \033[0mInterpreter compilation termined." && exit 1)
	mv tools/interpreter/tac-runner bin/ 
	echo -e "\n\033[1;36mInterpreter compilation successfully.\033[0m"

clean:
	rm ./bin/*
