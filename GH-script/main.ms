




test = {}
test.get_tokens = function(code)
	token = ""
	tokens = []

	for i in code
		if i == "\n" or i == ";" or white_space(i) then
			if i == "\n" then token

		end if
	end for
end function


get_tokens = function(code)
	code = code.replace("var ", "")
	code = code.replace(";", char(208))
	code = code.replace("ascy(", "char(")

	words = code.replace(char(10)," ").split(" ")
	lastInd = 0
	ind = 0
	for i in words
		// handal for loop
		if i == "for" then
			ind1 = ind
			while true
				if words[ind1].indexOf("{") != null then
					break
				end if
				ind1 = ind1 + 1
			end while
			args = words[ind+1:ind1+1].join(" ").replace("(", "").replace(")","").replace("{","").split(",")
			words[ind] = args[0] + char(208)
			words[ind+1] = "while"
			words[ind+2] = args[1] + char(208)
			forEnd = args[2] + char(208)
			words.remove(ind+4)
			words.remove(ind+3)
			ind2 = ind1
			while true
				if words[ind2].indexOf("}") != null then break
				ind2 = ind2 + 1
			end while
			words[ind2] = forEnd + "end while" + char(208)

		end if
		// handle +=
		ind1 = 0
		for a in i
			if a == "+" and i[ind1+1] == "=" and words[ind] == "+=" then
				words[ind] = " = " + words[ind-1] + " +"
			else if a == "+" and i[ind1+1] == "=" and words[ind][0] == "+" then
				words[ind] = " = " + words[ind-1].replace(char(9), "") + words[ind][1:-1]
			end if
			ind1 = ind1 + 1
		end for
		ind = ind + 1
	end for
	print(words.join(" ").replace(char(208),char(10)))
	return words.join(" ").replace(char(208),char(10))
end function


com = get_shell.host_computer

code = com.File("test.src").get_content

com.File("test.gms").set_content(get_tokens(code))
