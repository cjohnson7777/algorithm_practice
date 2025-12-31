import java.util.ArrayList;

public class NewsStation implements Observable{
    private ArrayList<Observer> subscribers = new ArrayList<>();
    private String headline;

    public NewsStation(String headline) {
        this.headline = headline;
    }

    public void add(Observer o) {
        subscribers.add(o);
    }

    public void remove(Observer o) {
        subscribers.remove(o);
    }
    
    public void notif() {
        for (Observer observer : subscribers) {
            observer.update();
        }
    }

    public String getHeadline() {
        return this.headline;
    }

}
