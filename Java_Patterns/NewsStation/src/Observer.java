public interface Observer {
    abstract void update();
}

class Display implements Observer {

    private NewsStation station;

    public Display(NewsStation station) {
        this.station = station;
    }

    @Override
    public void update() {
        System.out.println(station.getHeadline());
    }

    public static void main(String[] args) {
        NewsStation station = new NewsStation("Breaking");
        Display phone = new Display(station);
        station.add(phone);

        station.notif();
    }

}

