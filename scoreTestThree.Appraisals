#!/usr/bin/ruby
require 'colorize'

def v(score)
    success = false
	case score
        when 0
            #intro
            puts "Welcome to the guided security tour of Ubuntu :D".blue
            puts "You will be learning a few Unix skills along the way!".blue
            puts "Continue to run this program to get your score get the next task.".blue
            puts "When asked for input, simply type into this program.".blue
            puts "First Question: What user are you currently (find this using a command)?".white
            if gets.strip == "student"
                puts "Congratulations! You are student!.".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end
        
        when 1
         	#file path of sl
         	puts "What is the file path for the sl command?".white
         	if gets.strip == "/usr/games/sl"
         		puts "Congratulations! That is the correct file path!".green
         		return score + 1
         	else
         		puts "That is not the correct answer :(".white
         	end
         
        when 2
        	#history
		puts "How many times was the 'ls' command run in the history of this vm?(check the history and do not count the instances you use ls to search!)".white	
        	if gets.strip == `cat /home/student/.bash_history | grep 'ls' | wc -l`.chomp
			puts "Congratulations! That's the correct number!".green
                	return score + 1
            	else
                	puts "That is not the correct answer :("
            	end

        when 3
        	#sort -n
        	puts "There is a file of random numbers called numbers.txt in the myDir directory. What is the largest number in the file?".white
        	if gets.strip == "536546"
        		puts "Congratulations! That's the correct number!".green
                	return score + 1
            	else
            		puts "That's not the correct number. Try again!".white
            	end

        when 4
        	#uniq
        	puts "How many unique lines are in the numbers.txt file?".white
        	if gets.strip == "102"
        		puts "Congratulations! That's the correct number!".green
                	return score + 1
            	else
            		puts "That's not the correct number. Try again!".white
            	end

        when 5
        	#man
        	puts "What is the man page description for the who command?".white
        	if gets.strip == "Print information about users who are currently logged in."
        		puts "Congratulations! That's correct!".green
                	return score + 1
            	else
            		puts "That's not the correct description. Try again!".white
            	end

        when 6
        	#echo $PATH
        	puts "What is the command search path?"
        	if gets.strip == "/home/student/bin:/home/student/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
        		puts "Congratulations! That is the command search path!".green
                	return score + 1
            	else
                	puts "That's not the correct command search path.".white
            	end


        when 7
        	#bashrc
        	if `cat /home/student/.bashrc | grep "DELETE" | wc -l`.chomp.to_i == 0
                	puts "Congratulations! You accessed the .bachrc file and deleted the comment!".green
                	return score + 1
            	else
                	puts "Please go to the .bashrc file and delete the comment at the end of the file.".white
            	end

        when 8
        	#./
        	puts "Make the helloScript.py executable, run it, and print out the output."
        	if gets.strip == "hola"
        		puts "Congratulations! That's the correct output!".green
                	return score + 1
		else
            		puts "That's not the correct output. Try again!".white
            	end

        when 9
        	#>
        	puts "What symbol would you use to redirect standard output to a file?".white
        	if gets.strip == ">"
        		puts "Congratulations! That's correct!".green
                	return score + 1
           	else
            		puts "That's not the correct symbol. Try again!".white
            	end

        when 10
        	#<
        	puts "What symbol would you use to redirect standard input to a file?".white
        	if gets.strip == "<"
        		puts "Congratulations! That's correct!".green
                	return score + 1
            	else
            		puts "That's not the correct symbol. Try again!".white
            	end
		
	when 11
            puts "Congratulations! You've finished everything!! Keep practicing what we learned today! :D".blue
    end
    score
end

score = `cat /bin/loc.txt`.to_i

puts ("Old score: " + score.to_s).white

puts ""
score = v(score)
puts ""

score = score.to_s
`echo #{score} > /bin/loc.txt`
puts ("New score: " + score).white
