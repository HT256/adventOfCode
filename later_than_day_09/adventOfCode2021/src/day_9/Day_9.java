package day_9;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;


/**
 * Lösung für Tag 9.
 * 
 * @author Yanik Recke
 */
public class Day_9 {
	
	public static void main(String[] args) {
		String pathToInput = "src/Day_9/input.txt";
		
		System.out.println(part1(pathToInput) + " - " + part2(pathToInput));
	}
	
	
	/**
	 * Input in zweidimensionalen Array lesen 
	 * und Nachbarn der aktuellen Position 
	 * prüfen. Wenn kein Nachbar kleiner ist, dann
	 * Minimum gefunden.
	 * 
	 * @param path - Pfad zum Puzzle Input
	 * @return - Summe aller Risiko Level aller Tiefpunkte (Wert der Position + 1)
	 */
	private static int part1(String path) {
		int sum = 0;
		
		int[][] map = getInputAsTwoDimensionalArray(path);
		
		int tempX = 0;
		int tempY = 0;
		boolean min = true;
		
		for (int x = 0; x < map.length; x++) {
			for (int y = 0; y < map[x].length; y++) {
				tempX = x; 
				tempY = y - 1;
				if (isInbounds(map, tempX, tempY)) {
					if (map[tempX][tempY] <= map[x][y] && min) {
						min = false;
					}
				}
				
				tempX = x + 1; 
				tempY = y;
				if (isInbounds(map, tempX, tempY)) {
					if (map[tempX][tempY] <= map[x][y] && min) {
						min = false;
					}
				}
				
				tempX = x; 
				tempY = y + 1;
				if (isInbounds(map, tempX, tempY)) {
					if (map[tempX][tempY] <= map[x][y] && min) {
						min = false;
					}
				}
				
				tempX = x - 1; 
				tempY = y;
				if (isInbounds(map, tempX, tempY)) {
					if (map[tempX][tempY] <= map[x][y] && min) {
						min = false;
					}
				}
				
				if (!min) {
					min = true;
				} else {
					sum += map[x][y] + 1;
				}
			}
		}
		
		return sum;
	}
	
	
	/**
	 * Jede Position durchgehen, wenn eine Position, die
	 * noch nicht geprüft wurde und ungleich Null ist, gefunden wurde,
	 * zu toCheck hinzufügen. Alle Nachbarn der Positon prüfen, ob
	 * ungleich Neun, noch nicht geprüf, inbounds und nicht in toCheck,
	 * dann zu toCheck hinzufügen. Für jeden Durchlauf size + 1. Wenn
	 * kein Element mehr in toCheck vorhanden ist, nächste Position abarbeiten.
	 * 
	 * @param path - Pfad zum Puzzle Input
	 * @return - die Größe der größten 3 basins miteinander multipliziert
	 */
	private static int part2(String path) {
		int[][] map = getInputAsTwoDimensionalArray(path);
		List<Integer> sizesOfBasins = new ArrayList<>();
		Position current;
		
		
		int tempX = 0;
		int tempY = 0;
		
		int size = 0;
		
		List<Position> toCheck = new ArrayList<>();
		List<Position> alreadyChecked = new ArrayList<>();
		
		
		for (int x = 0; x < map.length; x++) {
			for (int y = 0; y < map[x].length; y++) {
				
				if (map[x][y] != 9 && !alreadyChecked.contains(new Position(x,y))) {
					toCheck.add(new Position(x,y));
				}
				
				while (!toCheck.isEmpty()) {
					current = toCheck.remove(0);
					size++;
					if (!alreadyChecked.contains(current)) {
						alreadyChecked.add(new Position(current.getX(), current.getY()));
					}
					
					tempX = current.getX();
					tempY = current.getY() - 1;
					if (isInbounds(map, tempX, tempY) && !alreadyChecked.contains(new Position(tempX, tempY)) && map[tempX][tempY] != 9 && !toCheck.contains(new Position(tempX, tempY))) {
						toCheck.add(new Position(tempX, tempY));
					}
					
					tempX = current.getX() + 1;
					tempY = current.getY();
					if (isInbounds(map, tempX, tempY) && !alreadyChecked.contains(new Position(tempX, tempY)) && map[tempX][tempY] != 9 && !toCheck.contains(new Position(tempX, tempY))) {
						toCheck.add(new Position(tempX, tempY));
					}
					
					tempX = current.getX();
					tempY = current.getY() + 1;
					if (isInbounds(map, tempX, tempY) && !alreadyChecked.contains(new Position(tempX, tempY)) && map[tempX][tempY] != 9 && !toCheck.contains(new Position(tempX, tempY))) {
						toCheck.add(new Position(tempX, tempY));
					}
					
					tempX = current.getX() - 1;
					tempY = current.getY();
					if (isInbounds(map, tempX, tempY) && !alreadyChecked.contains(new Position(tempX, tempY)) && map[tempX][tempY] != 9 && !toCheck.contains(new Position(tempX, tempY))) {
						toCheck.add(new Position(tempX, tempY));
					}
				}
				
				sizesOfBasins.add(size);
				size = 0;
			}
		}
		
		sizesOfBasins.sort(Comparator.reverseOrder());
		return sizesOfBasins.get(0) * sizesOfBasins.get(1) * sizesOfBasins.get(2);
	}
	
	
	/**
	 * Prüft ob eine Position in den Grenzen eines 
	 * Arrays liegt.
	 * 
	 * @param arr - der Array
	 * @param x - x-Koordinate
	 * @param y - y-Koordinate
	 * @return - true, wenn Koordinaten innerhalb liegen, false wenn nicht
	 */
	private static boolean isInbounds(int[][] arr, int x, int y) {
		return x >= 0 && y >= 0 && x < arr.length && y < arr[x].length;
	}
	
	
	/**
	 * Liest einen Input in einen 
	 * mehrdimensionalen Array von Integern.
	 * 
	 * @param path - Pfad zur Datei
	 * @return - mehrdimensionaler Array an Integern
	 */
	public static int[][] getInputAsTwoDimensionalArray(String path) {
		assert (path != null);

		int[][] input;
		int i = 0;
		int j = 0;
		
		try (BufferedReader br = new BufferedReader(new FileReader(path))) {
		    String line = br.readLine();
		    j = line.length();
		    
		    while (line != null) {
		        i++;
		        line = br.readLine();
		    }

		} catch (Exception e) {
			e.printStackTrace();
		} 
		
		input = new int[j][i];
		
		i = 0;
		j = 0;
		
		try (BufferedReader br = new BufferedReader(new FileReader(path))) {
		    String line = br.readLine();
		    
		    while (line != null) {
		    	
		    	for (int k = 0; k < line.length(); k++) {
		    		input[k][i] = line.charAt(k) - '0';
		    	}
		    	
		    	line = br.readLine();
		        i++;
		        
		    }

		} catch (Exception e) {
			e.printStackTrace();
		} 
		
		return input;
	}
}
