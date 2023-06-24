import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SearchQue implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label1 = new JLabel();
    JLabel label2 = new JLabel();
    JTextField text = new JTextField();
    JButton button = new JButton();
    JButton button1 = new JButton();
    int num;
    int n;
    int a[];
    int pos = 0;

    SearchQue(int ar[], int index, JFrame frame1){

        a = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            a[f] = ar[f];
        }

        label1.setText("Search by: ");
        label1.setVisible(true);
        label1.setBounds(15, 5, 100, 30);
        label1.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        button.setText("Position");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(90, 40, 150, 28);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 15));
        button.addActionListener(this);

        button1.setText("Number");
        button1.setVisible(true);
        button1.setFocusable(false);
        button1.setBounds(90, 75, 150, 28);
        button1.setFont(new Font("Times New Roman", Font.PLAIN, 15));
        button1.addActionListener(this);

        frame.setTitle("Search");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("search.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label1);
        frame.add(button);
        frame.add(button1);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            frame.dispose();
            SearchPage1 search = new SearchPage1(a, n);
        }
        if(e.getSource() == button1){
            frame.dispose();
            SearchPage2 search = new SearchPage2(a, n);
        }
    }
}
