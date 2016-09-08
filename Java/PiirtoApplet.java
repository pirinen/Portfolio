import java.applet.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

	//Jukka Pirinen 8.9.2016
public class tehtava2 extends Applet
	implements KeyListener, MouseListener
{
	Color vari;		//väri
	int x,y;		//koordinaattien muuttujat
	boolean piirto = false;	//jos halutaan että: "Piirtäminen tapahtuu, kun käyttäjä on valinnut hiirellä kohdan ja näppäimellä värin.". //lisäosa
	
	public void init()
	{
		setBackground(Color.white);	//taustaväri
		
		addMouseListener(this);	//hiiren ja
		addKeyListener(this);	//näppäimistön kuuntelijat
	}
	
	public void mouseReleased(MouseEvent e)	//Hiiren vapautus alkaa
	{
		requestFocus();	//focus tähän
		x = e.getX();	//luetaan klikkauksen x koordinaatin arvo muistiin
		y = e.getY();	//luetaan klikkauksen y koordinaatin arvo muistiin
		repaint();		//piirretään kuvio uudelleen
		
	}	//Hiiren vapautus loppuu
	
	public void paint(Graphics g)
	{	
		//piirretään ohjeet käyttäjälle alkaa
		g.setColor(Color.blue);
		g.fillRect(10, 10, 80, 20);
		g.setColor(Color.black);
		g.drawString("s=sininen", 20, 25);
		
		g.setColor(Color.red);
		g.fillRect(100, 10, 80, 20);
		g.setColor(Color.black);
		g.drawString("p=punainen", 110, 25);
		
		g.setColor(Color.yellow);
		g.fillRect(190, 10, 80, 20);
		g.setColor(Color.black);
		g.drawString("k=keltainen", 200, 25);
		
		g.setColor(Color.green);
		g.fillRect(280, 10, 80, 20);
		g.setColor(Color.black);
		g.drawString("v=vihreä", 290, 25);
		//piirretään ohjeet käyttäjälle loppuu
		
		//if (piirto == true)	//ei piirrä mitään ennenkuin väri on valittu. //lisäosa
		{	//varsinainen tehtävän piirto alkaa
			g.setColor(vari);	//asetetaan väri
			g.fillRect(x-20, y-20, 20, 20);	//piirretään neliö
		}	//varsinainen tehtävän piirto loppuu
		
	}
	
	public void keyTyped(KeyEvent e)	//Värin valinta alkaa
	{
		char valinta = e.getKeyChar();	//luetaan näppäimen painallus talteen
	
		switch (valinta)	//mennään tarkastamaan mitä näppäintä painettiin
		{		//Toimii myös Caps Lock päällä
		case 's': case 'S': vari = Color.blue; repaint(); 			//piirto = true;	//lisäosa
			break;	//sininen
		case 'p': case 'P': vari = Color.red; repaint(); 			//piirto = true;	//lisäosa
			break;	//punainen
		case 'k': case 'K': vari = Color.yellow; repaint(); 		//piirto = true; //lisäosa
			break;	//keltainen
		case 'v': case 'V': vari = Color.green; repaint(); 			//piirto = true; //lisäosa
			break;	//vihreä
		default : vari = Color.black; repaint();	//jos joku muu nappi, niin musta
			break;
		}
	}	//Värin valinta loppuu

	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void keyPressed(KeyEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyReleased(KeyEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}

	//Laadi appletti, joka toimii seuraavasti. Kun klikkaat hiirellä johonkin kohti 
	//appletin alueella, piirtää appletti kyseiseen kohti 20 pikselin suuruisen neliön, 
	//joka on halutunvärinen. Värin käyttäjä valitsee painamalla hiiren klikkaamisen 
	//jälkeen jotain seuraavista painikkeista: s=sininen, p=punainen, k=keltainen tai v=vihreä. 
	//Piirtäminen tapahtuu, kun käyttäjä on valinnut hiirellä kohdan ja näppäimellä värin.
