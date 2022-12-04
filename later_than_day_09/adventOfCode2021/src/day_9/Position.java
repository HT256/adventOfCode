package day_9;


public class Position {
	private int x = 0;
	private int y = 0;
	
	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public int getX() {
		return this.x;
	}
	
	public int getY() {
		return this.y;
	}
	
	@Override
	public boolean equals(Object obj) {
		return obj != null && ((Position) obj).getX() == this.x && ((Position) obj).getY() == this.y;
	}
}
