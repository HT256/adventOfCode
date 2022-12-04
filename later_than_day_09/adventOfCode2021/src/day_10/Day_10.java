package day_10;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Lösung für Tag 10.
 * 
 * @author Yanik Recke
 */
public class Day_10 {

	public static void main(String[] args) {
		String pathToInput = "src/day_10/input.txt";
		
		System.out.println(part1(pathToInput) + " - " + part2(pathToInput));
	}
	
	
	/**
	 * Liste pflegen mit allen öffnenden Zeichen.
	 * Wenn ein schließendes Zeichen kommt, prüfen ob das
	 * letzte öffnenden das dazu passende war. 
	 * 
	 * @param path - Pfad zum Puzzle Input
	 * @return - der Syntax Error Score
	 */
	private static int part1(String path) {
		// TODO wäre besser mit Queue
		int score = 0;
		List<String> open = new ArrayList<>();
		
		Set<Character> openings = new HashSet<>();
		openings.addAll(Arrays.asList('(', '[', '{', '<'));
		
		try (BufferedReader br = new BufferedReader(new FileReader(path))) {
		    String line = br.readLine();

		    while (line != null) {
		    	int i = 0;
		    	boolean error = false;
		    	
		    	while(i < line.length() && !error) {
		    		if (openings.contains(line.charAt(i))) {
		    			open.add("" + line.charAt(i));
		    		} else {
		    			switch(line.charAt(i)) {
		    				case ')' -> {
		    					if (error = !open.get(open.size() - 1).equals("(")) {
		    						score += 3;
		    					} else {
		    						open.remove(open.size() - 1);
		    					}
		    				}
		    				
		    				case ']' -> {
		    					if (error = !open.get(open.size() - 1).equals("[")) {
		    						score += 57;
		    					} else {
		    						open.remove(open.size() - 1);
		    					}
		    				}
		    				
		    				case '}' -> {
		    					if (error = !open.get(open.size() - 1).equals("{")) {
		    						score += 1197;
		    					} else {
		    						open.remove(open.size() - 1);
		    					}
		    				}
		    				
		    				default -> {
		    					if (error = !open.get(open.size() - 1).equals("<")) {
		    						score += 25137;
		    					} else {
		    						open.remove(open.size() - 1);
		    					}
		    				}
		    			}
		    		}

		    		i++;
		    	}
		    	
		        line = br.readLine();
		    }

		} catch (Exception e) {
			e.printStackTrace();
		} 
		
		return score;
	}
	
	
	/**
	 * Zuerst entfernen der korrupten Zeilen, dann
	 * prüfen, welche Openings über bleiben.
	 * Wäre besser mit Queue.
	 * 
	 * @param path - Pfad zum Puzzle Input
	 * @return - Mittelgroßer Score
	 */
	private static long part2(String path) {
		Long score = 0L;
		List<Long> scores = new ArrayList<>();
		List<String> lines = removeCorruptLines(path);
		List<String> open = new ArrayList<>();
		
		Set<Character> openings = new HashSet<>();
		openings.addAll(Arrays.asList('(', '[', '{', '<'));
		int i = 0;

		for (String line : lines) {
			i = 0;
	    	while(i < line.length()) {
	    		if (openings.contains(line.charAt(i))) {
	    			open.add("" + line.charAt(i));
	    		} else {
	    			switch(line.charAt(i)) {
	    				case ')' -> {
	    					if (open.get(open.size() - 1).equals("(")) {
	    						open.remove(open.size() - 1);
	    					}
	    				}
	    				
	    				case ']' -> {
	    					if (open.get(open.size() - 1).equals("[")) {
	    						open.remove(open.size() - 1);
	    					}
	    				}
	    				
	    				case '}' -> {
	    					if (open.get(open.size() - 1).equals("{")) {
	    						open.remove(open.size() - 1);
	    					} 
	    				}
	    				
	    				default -> {
	    					if (open.get(open.size() - 1).equals("<")) {
	    						open.remove(open.size() - 1);
	    					}
	    				}
	    				
	    			}
	    		}
	    		i++;
	    	}
	    	
	    	score = 0L;
	    	for (int j = open.size() - 1; j >= 0; j--) {
	    		score = score * 5;
	    		
	    		switch(open.get(j)) {
	    			case "(" -> {
	    				score += 1;
	    			}
	    			
	    			case "[" -> {
	    				score += 2;
	    			}
	    			
	    			case "{" -> {
	    				score += 3;
	    			}
	    			
	    			default -> {
	    				score += 4;
	    			}
	    		}
	    	}
	    	
	    	scores.add(score);
	    	open = new ArrayList<>();
		}
		
		scores.sort(Comparator.naturalOrder());

		return scores.get(scores.size() / 2);
	}
	
	
	/**
	 * Entfernt die korrupten Zeilen.
	 * 
	 * @param path - Pfad zum Puzzle Input
	 * @return - Liste ohne korrupte Zeilen
	 */
	private static List<String> removeCorruptLines(String path){
		List<String> open = new ArrayList<>();
		
		Set<Character> openings = new HashSet<>();
		openings.addAll(Arrays.asList('(', '[', '{', '<'));
		
		List<String> nonCorruptedLines = new ArrayList<>();
		
		try (BufferedReader br = new BufferedReader(new FileReader(path))) {
		    String line = br.readLine();

		    while (line != null) {
		    	int i = 0;
		    	boolean error = false;
		    	
		    	while(i < line.length() && !error) {
		    		if (openings.contains(line.charAt(i))) {
		    			open.add("" + line.charAt(i));
		    		} else {
		    			
		    			switch(line.charAt(i)) {
		    				case ')' -> {
		    					if (open.get(open.size() - 1).equals("(")) {
		    						open.remove(open.size() - 1);
		    					} else {
		    						error = true;
		    					}
		    				}
		    				
		    				case ']' -> {
		    					if (open.get(open.size() - 1).equals("[")) {
		    						open.remove(open.size() - 1);
		    					} else {
		    						error = true;
		    					}
		    				}
		    				
		    				case '}' -> {
		    					if (open.get(open.size() - 1).equals("{")) {
		    						open.remove(open.size() - 1);
		    					} else {
		    						error = true;
		    					}
		    				}
		    				
		    				default -> {
		    					if (open.get(open.size() - 1).equals("<")) {
		    						open.remove(open.size() - 1);
		    					} else {
		    						error = true;
		    					}
		    				}
		    				
		    			}
		    		}

		    		i++;
		    	}
		    	
		    	if (!error) {
		    		nonCorruptedLines.add(line);
		    	}
		    	
		        line = br.readLine();
		    }

		} catch (Exception e) {
			e.printStackTrace();
		} 
		
		return nonCorruptedLines;
	}
	
	
}
