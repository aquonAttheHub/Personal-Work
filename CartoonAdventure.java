import java.util.Scanner;
import java.util.Random;

public class FirstClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*Resources:
		 while loops
		 integers and other data types
		 for loops
		 if statements
		 input (Scanner)
		 Random
		 
		 Ideas:
		 Combat type game ~ "dragon's lair" or "the guard"
		 Name: Spongebob's King of Karate: Island Showdown
		 Player: Spongebob, Sandy, Mermaidman, Barnacle Boy
		 1st opponent: The Tickler
		 2nd opponent: Lip Service
		 3rd opponent: Filthy Phil
		 4th opponent: Plankton
		 5th opponent: Fuzzy
		 Boss: Master Udon  
		 # of levels: 6, including boss level.
		 */
		Random randomGenerator = new Random();
		System.out.println("Welcome to 1v1 tower!");
		System.out.println(" Your title, The Supreme Nautical Warrior, awaits you!");
		System.out.println("But first, you must demonstrate your bravery and fighting skills by defeating the most formidable of foes who would stop at nothing to stop you!" );
		System.out.println("If you suceed, you shall receive a 5 year supply of krabby patties and a new condo with a panoramic view of the island!");
		int playerLevel = 0;
		double playerHealth = 100.0;
		String playerSentiment;
		
		//TODO1: Import Scanner to read input, which will be the name of the chosen character.
		Scanner userInput;
		
		userInput = new Scanner(System.in);
		System.out.println("Choose your character.");
		System.out.println("1.Spongebob Squarepants.");
		System.out.println("2.Sandy Cheeks.");
		int playerChar;
		playerChar = userInput.nextInt();
		if(playerChar == 1) {
			System.out.println("Greetings Spongebob");
			
		}else if(playerChar == 2) {
			System.out.println("Greetings Sandy");
		}
		
		System.out.println("What is your real name?");
		String playerName = userInput.next();
		System.out.println("Welcome " + playerName);
		
		//Proceed on to mood check.
		
		//System.out.println("Has this been your first time playing?");
		//playerSentiment = userInput.nextLine();
		//System.out.println("Well, " + playerSentiment + " is a great answer");
		
		int playerChoice;
		System.out.println("How do you feel about fighting today to fulfill your destiny as supreme warrior?");
		System.out.println("1. Great! This is going to be the best day of my life.");
		System.out.println("2. As long as I can eat all day and enjoy paradise, I will fight.");
		System.out.println("3. Barnacles! Don't feel confident. I'll just go to Goo Lagoon or Fancy Springs to get my luxuries.");
		System.out.println("4. Horrible. I ain't spending my last day fighting some menacing bottom feeders.");
		playerChoice = userInput.nextInt();
		if(playerChoice == 1 || playerChoice == 2){
			//The player enters the cave
			System.out.println("Excellent. Let the showdown begin!");
			playerLevel++;
		
		}else {
				System.out.println("How unfortunate...game over for you.");
				System.exit(0);
			
			}	
			
			System.out.println("Your bravery has rewarded you! Congradulations, you are now level " + playerLevel);
			System.out.println("You walk into the first floor of Mater Udon's dreaded tower." );
			System.out.println("'HALT!' shouts The Tickler. 'Nobody passes the The Tickler. Prepare for the tickling of your life!' ");
			System.out.println("You respond...");
			System.out.println("1. 'Bring it on!'");
			System.out.println("2. 'I give up now.' You retreat home with the sad feeling that you will have to pay Mr. Krabs money for a krabby patty.");
			playerChoice = userInput.nextInt();
			if(playerChoice == 1) {
				System.out.println("'It's on now', says The Tickler. ");
				System.out.println("Make your move.");
				System.out.println("1. Karate chop The Tickler on the head");
				System.out.println("2. Wait for The Tickler to reach you with his arm sticks, swipe the sticks off his hands, and tickle him to show who's boss");
				System.out.println("3. Point to the ceiling to distract him, saying 'Look! There's an eagle!'");
				playerChoice = userInput.nextInt();
				if(playerChoice == 1 || playerChoice == 2) {
					System.out.println("'Ouf!'");
					System.out.println("'Ow! He he he, that tickles.'");
					System.out.println("'Hiyah!'");				
					int damageToPlayer;
					damageToPlayer = randomGenerator.nextInt(10);
					playerHealth -= damageToPlayer;
					System.out.println("The Tickler attacks you for " + damageToPlayer+ "!");					
					System.out.println("You have " + playerHealth + " health remaining.");
					System.out.println("You have defeated The Tickler.");
					playerLevel++;
				
				
					//Proceed to next level
					System.out.println("Congradulations! You have made it to the second floor...");
					System.out.println("Behold! Lip Service strikes with her extremely long and elastic lips." );
					System.out.println("'Kissy Kissy', Lip Service hisses.");
					String playerSay;
					System.out.print("Insult her by calling her something; this should be one word.");
					playerSay = userInput.next();
					System.out.println("Arrrrrgh!");
					System.out.println("Make your move.");
					System.out.println("1. Kiss Lip Service because you think she's pretty and faint to a powerful potion.");
					System.out.println("2. Use a blow dryer to dry her wet, elastic lips.");
					System.out.println("3. Lunge at the enemy and throw her a good punch.");
					playerChoice = userInput.nextInt();
					if(playerChoice == 1 && playerChar == 1) {
						System.out.println("'Nighty Night Squarepants!' shouts Lip Service.");
						System.out.println("Game Over.");
						System.exit(0);
					}else if(playerChoice == 1 && playerChar == 2) {
						System.out.println("MWAH!");
						System.out.println("'Good night Sandy Cheeks' gloats Lip Service.'Why would you want to kiss me anyway? You're a girl.'");
						System.out.println("Game Over.");
						System.exit(0);
					}
					else if(playerChoice == 2) {
						damageToPlayer = randomGenerator.nextInt(10);
						playerHealth -= damageToPlayer;
						System.out.println("Lip Service attacks you for " + damageToPlayer + "!");						
						System.out.println("'Activate blowdryer!'");
						System.out.println("'Arrrrgh' cries Lip Service as she watches her long lips dry up and crumble before her" );
						System.out.println("You have defeated Lip Service");
						System.out.println("You have " + playerHealth + " health remaining.");
						playerLevel++;
					} else if(playerChoice == 3) {
						System.out.println("'Take that!'you say.");
						System.out.println("'Argghhhhhhhhhhhaaaaa!");
						System.out.println("Your hand becomes stuck in her lips and you feel your whole arm being sucked in!");
						playerHealth = playerHealth - 10;
						System.out.println("Lip Service attacks you for " + damageToPlayer + "!");
						System.out.println("But your resilient and you throw her another punch as her lips draw you near her");
						System.out.println("Down she falls. You have defeated Lip Service!");
						System.out.println("You have " + playerHealth + " remaining!");
						playerHealth++;
					}
						
						
						//Proceed with the game.
						System.out.println("Congradulations! You've made it to the 3rd level");
						System.out.println("Prepare to meet Filthy Phil!");
						System.out.println("You ascend to the 3rd floor and find that is is extremely dank and odorous");
						System.out.println("Ewww...what is that smell?");
						if(playerChar == 1) {
							System.out.println("'That's me you square-headed bobby!' says Filthy Phil as he emerges from the dark");								
						}
						else if(playerChar == 2) {
							System.out.println("'That's me you bubble-headed lassie!' says Filthy Phil as he emerges from the dark");
						}
						System.out.println("'Dare to step through the filthy lair of Filthy Phil?'");
						System.out.println("1. Cover your nose and drive your foot into your enemy");					
						System.out.println("2. Redirect his odor so that he smells his own filth");
						playerChoice = userInput.nextInt();
						if(playerChoice == 1) {
							System.out.println("Yikes, you find your foot stuck on his belly and he wraps you in a warm embrace, jabbing your head on his belly");
							playerHealth = playerHealth - 50;
							System.out.println("Your health drops by 50!");
							System.out.println("You eventually break loose and break his nose, defeating him");
							System.out.println("You have " + playerHealth + " remaining.");
							playerLevel++;
						
						}
						else if(playerChoice == 2) {
							System.out.println("The odors penetrate Filthfy Phil's nose. His eyes water and he admits he stinks, then loses consciousness." );
							System.out.println("You have defeated Filthy Phil!");
							System.out.println("You have " + playerHealth+ " remaining.");					
							playerLevel++;	
						}
						//Proceed to next level
						System.out.println("You have made it to the next level.");
						System.out.println("Prepare to meet...Plankton!");
						System.out.println("'Plankton!' you shout in disbelief.");
						if(playerChar == 1) {
							System.out.println("'YES MR. SQUAREPANTS! ONCE I DEFEAT YOU, I WILL TAKE THE KRABBY PATTIES TO THE CHUM BUCKET AND RUN THE KRUSTY KRAB OUT OF BUSINESS!");
							System.out.println("Plankton shows up in his combat robot");
							
						}else if(playerChar == 1) {
							System.out.println("'YES YOU SQUIRREL! ONCE I DEFEAT YOU, I WILL TAKE THE KRABBY PATTIES TO THE CHUM BUCKET AND RUN THE KRUSTY KRAB OUT OF BUSINESS!");
							System.out.println("As a bonus, I will destroy your tree dome and take your science equipment!");
							System.out.println("Plankton shows up in his combat robot");
						}
						System.out.println("A cannon emerges from the robot's belly and shoots mayonaise at your direction");
						System.out.println("'Feel my Wrath!' shouts Plankton");
						if(playerChar == 1) {
							System.out.println("1. Be a true sponge by absorbing the mayonaise, growing into a mega-karate-mayonaise-squirting machine!");
							System.out.println("2. You morph into mermaidman and throw dynamic waterballs at the robot to disable its circuits");
							System.out.println("3. Dodge the mayonaise, take out your beloved spatula, and serve your enemy up with forcefull blows of patty projectiles");
							playerChoice = userInput.nextInt();
							if(playerChoice == 1) {
								System.out.println("You grow in size until you dwarf plankton's robot.");
								System.out.println("WHAT! CURSES! NOOOOOOOOOO...");
								System.out.println("You return the mayonaise to its sender and plankton is pushed back through the wall and falls into the ocean.");
								System.out.println("You have defeated plankton!");
								System.out.println("You have " + playerHealth + " remaining!");
								playerLevel++;
								
							}else if(playerChoice == 2) {
								System.out.println("Mermaidman's theme plays as you use your superpower to deflect the mayonaise.");
								System.out.println("You thrust forward and deliver to plankton the whack of his life.");
								System.out.println("WHACK! OUCH! OOOH! POW!");
								System.out.println("Plankton uses his metal claws in an attempt to strike you, but you send in a waterball just in time, disabling his circuits" );
								System.out.println("You perform a mae geri kekomi and kick plankton out of the tower!");
								System.out.println("You have defeated plankton!");
								System.out.println("You have " + playerHealth + " remaining!");
								playerHealth++;
							}else if(playerChoice == 3) {
								System.out.println("'Oh dear!' cries plankton");
								System.out.println("You launch patties forward to penetrate plankton's armor.");
								System.out.println("One of the patties takes a headshot to the robot, where plankton is controlling the robot.");
								System.out.println("Plankton is ejected from the cockpit and you defeat him with a final chop");
								System.out.println("You have defeated plankton!");
								System.out.println("You have " + playerHealth + " remaining!");
								playerHealth++;
							}
						}else if(playerChar == 2) {
								System.out.println("1. Be a true karate warrior and take a forceful chop!");								
								System.out.println("2. Dodge the mayonaise, take out your rodeo gear, restrain the robot");
								playerChoice = userInput.nextInt();
								if(playerChoice == 1) {
									System.out.println("Hiyah!");
									System.out.println("NOOOOOOOOOO...");
									System.out.println("Plankton's robot cuts in half and plankton flees.");
									System.out.println("You have defeated plankton!");
									System.out.println("You have " + playerHealth + " remaining!");
									playerLevel++;
									
								}else if(playerChoice == 2) {
									System.out.println("'Let's do this Texas style!'");
									System.out.println("'Bring it on, Landy!' cries Plankton.");
									System.out.println("You form a lasso and restrain the robot's arms. You then jerk your rope to launch him out the window.");					
									System.out.println("You have defeated plankton!");
									System.out.println("You have " + playerHealth + " remaining!");
									playerLevel++;
								}
								
								}
						//Proceed to next level
						System.out.println("Congradulations, you have made it to boss level!");
						System.out.println("'Greetings!' says Master Udon with a warm smile. 'You have defeated all my warriors.'");
						System.out.println("'I ain't playing any games!' you shout");
						System.out.println("His countenance suddenly changes to that of a belligerent and sadistic man");
	
						System.out.println("Well then, give into my powerful fists");
						System.out.println("1.Jump on top of the enemy and let his head rebound between simultaneous kicks");
						System.out.println("2.Punch the enemy");
						playerChoice = userInput.nextInt();
						if(playerChoice == 1);
							System.out.println("You jump on top of him and kick him several times.");
							System.out.println("But he grabs your ankles and throws you at the wall");
							damageToPlayer = randomGenerator.nextInt(30);
							playerHealth -= damageToPlayer;
							System.out.println("Master Udon attacks you for " + damageToPlayer);
							System.out.println("1. Spring from the wall and pin him down.");
							System.out.println("2. Charge towards the Master and trip him." );
							playerChoice = userInput.nextInt();
							if(playerChoice == 1) {
								System.out.println("You pin him down with force, keeping his head below you and his arms behind his back.");
								System.out.println("As his energy drains, you say something to him");
								System.out.print("What do you say? Call him something in one word.");
								//Anything you want
								playerName = userInput.next();
								System.out.println("Goodbye Master Udon, " + playerName);
								System.out.println("Congradulations, you have earned the title The Supreme Nautical Warrior!");
								System.out.println("You will receive a 5 year supply of krabby patties and an oceanside condo!");
								
								
							}
							else {
								damageToPlayer = randomGenerator.nextInt(30);
								playerHealth -= damageToPlayer;
								System.out.println("Master Udon catches you and attacks you for " + damageToPlayer);
								System.out.println("You have " + playerHealth + " remaining");
								System.out.println("Don't give up. Keep fighting!");
								System.out.println("Make your move.");
								System.out.println("1. Super smackdown");
								System.out.println("2. Give up");
								playerChoice = userInput.nextInt();
								if(playerChoice == 1) {
									System.out.println("Poof poof poof! You defeat Master Udon!");
									System.out.println("Congradulations, you have earned the title The Supreme Nautical Warrior!");
									System.out.println("You will receive a 5 year supply of krabby patties and an oceanside condo!");
								}
								else {
									System.out.println("You were so close to claiming the title! Barnacles to you!");
									System.exit(0);
								}
								
							}
						
								
								
								
						}
					
							
						
						
						
						
						
					
					
					
					
					
					
					
					}
					else if(playerChoice == 3) {
						System.out.println("'Hiyah!");
						System.out.println("Lip Service thwarts your attack!");
						System.out.println("'Ha!' cries Lip Service. 'You are no match for my extraordinary lip powers!'");
						playerHealth = playerHealth - 30;
						System.out.print("Lip Service attacks you for 30!");
						System.out.println("Do you wish to continue?");
						System.out.println("1. Yes");
						System.out.println("2. No");
						playerChoice = userInput.nextInt();
						if(playerChoice == 1) {
							System.out.println("You're too weak and Lip Service knocks you out");
							System.exit(0);
						}
						else {
							System.out.println("'Well then, prepare to be destroyed' cries Lip Service");
							System.out.println("You throw a blow at her but she catches your punch again");
							System.out.println("Lip Service knocks you out");
							System.exit(0);
						}
						
						
				}else if(playerChoice == 3) {
					System.out.println("'Ha!' says The Tickler. 'Les aigles n'existent pas sous l'eau.'");
					System.out.println("'Noooooooooo!'");
					System.out.println("The Tickler has defeated you! Game over!");
					System.exit(0);
	}				
					
						
					
					
				
					
				

				
			}
			
			
		/*else {
			System.out.println("How unfortunate...game over for you.");
			System.exit(0);
		
		}*/
		
	}		
	




