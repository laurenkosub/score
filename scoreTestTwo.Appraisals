#!/usr/bin/ruby
require 'colorize'

def v(score)
    success = false
	case score
        when 0
            #intro
            puts "Welcome to the guided tour of Unix :D".white
            puts "You will be practicing what you learned today by answering questions and accomplishing different tasks!".white
            puts "Continue to run this program to answer questions, score points, and get to the next task.".white
            puts "When asked for input, simply type into this program.".white
            #sudo
            puts "Let's begin: What does sudo stand for?".white
            if gets.strip == "super user do"
                puts "Congratulations! You got the question right! :)".yellow
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end
        
        #install sl
        when 1
            if `cat /var/log/auth.log | grep 'apt-get install sl' | grep -v grep | wc -l`.chomp.to_i != 0
                puts "Congratulations! You installed sl. Don't forget to try out the command!".green
                return score + 1
            else
                puts "Install sl through the terminal and run the command once you're done.".white
            end

        #upgrade
        when 2
            puts "What do you put into the terminal to upgrade the system?".white
            if gets.strip == "sudo apt-get upgrade"
                puts "Congratulations! That's the correct command :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

         #update
         when 3
            if `cat /var/log/auth.log | grep 'apt-get update' | grep -v grep | wc -l`.chomp.to_i != 0
                puts "Congratulations! You updated the system.".green
                return score + 1
            else
                puts "It looks like this system hasn't been updated in a while. Could you update it?".white
            end
        
        #uninstall
         when 4
            if `cat /var/log/auth.log | grep 'apt-get purge ftp' | grep -v grep | wc -l`.chomp.to_i != 0
                puts "Congratulations! You uninstalled ftp.".green
                return score + 1
            else
                puts "Uninstall ftp.".white
            end

        #grep
        when 5
            puts "What command do you use to search a file?".white 
            if gets.strip == "grep"
                puts "Congratulations! That's the correct command :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

         #piping
        when 6
            puts "What symbol represents piping in Unix?".white 
            if gets.strip == "|"
                puts "Congratulations! That's the correct symbol :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end        

        #search "lauren"
        when 7
            puts "How many times does 'lauren' appear in the names.txt file in the myDir directory?".white 
            if gets.strip == "3"
                puts "Congratulations! That's the correct command :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        #search pass
        when 8
            puts "How many times does 'pass' appear in the passwords.txt file in the myDir directory? Hint: this file is longer and has more instances of 'pass' so pipe wc -l to determine the word count of 'pass'".white 
            if gets.strip == "34"
                puts "Congratulations! That's the correct number :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        #crontab
         when 9
	    puts "What command do you use to edit the crontab?"
	    if gets.strip == "crontab -e"
                puts "Congratulations! Now use that command to add a comment in the crontab.".green
                return score + 1
            else
                puts "Wrong command. Try again!!".white
            end

        #chmod
        when 10
            puts "What command do you use to change access permissions to file system objects?".white 
            if gets.strip == "chmod"
                puts "Congratulations! That's the correct command :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        #777
        when 11
            puts "What number combination gives the file read, write, and execution permission for everyone?".white 
            if gets.strip == "777"
                puts "Congratulations! That's the correct combo :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        when 12
            puts "How do you make p represent the command \"pwd\" using an alias?".white 
            if gets.strip == "alias p=\"pwd\""
                puts "Congratulations! That's the correct answer :)".green
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        when 13
            puts "Congratulations! You've finished everything!! keep practicing the things we learned today by making/manipulating files!".blue
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
