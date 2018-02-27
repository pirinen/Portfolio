using UnityEngine;
using UnityEngine.VR.WSA.Input;
//using UnityEngine.VR.WSA.Input;

public class script : MonoBehaviour
{
    GameObject obj;
    Material m_Material;
    private GestureRecognizer gestureRecognizer;    public RaycastHit hit;    public Ray ray;
    private void Start()
    {
        // m_Material = GetComponent<Renderer>().material;

        //Set up GestureRecognizer to register user's finger taps
        gestureRecognizer = new GestureRecognizer();
        gestureRecognizer.TappedEvent += GestureRecognizer_TappedEvent;
        gestureRecognizer.SetRecognizableGestures(GestureSettings.Tap);
        gestureRecognizer.StartCapturingGestures();
    }

    private void GestureRecognizer_TappedEvent(InteractionSourceKind source, int tapCount, Ray headRay)
    {
        Debug.Log("finger movement");

        if (Physics.Raycast(headRay, out hit, 100.0f))
        {

            changeColor();
        }
    }

    private void Update()
    {
        ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        if (Input.GetMouseButtonDown(0))
        {
            //Debug.Log("Mouse down");
            
            if (Physics.Raycast(ray, out hit, 100.0f))
            {
                //Debug.Log("raycast");

                ray = Camera.main.ScreenPointToRay(Input.mousePosition);
                obj = hit.transform.gameObject;
                Debug.Log(obj + " " + hit.point + obj.GetComponent<Renderer>().material.color);
                if (obj.GetComponent<Renderer>().material.color != Color.green)
                {
                    if (obj.GetComponent<Renderer>().material.color == Color.red)
                        obj.GetComponent<Renderer>().material.color = Color.white;
                    else
                        obj.GetComponent<Renderer>().material.color = Color.red;
                }
                //changeColor();
            }


        }

        if (Input.GetMouseButtonDown(2))
        {
            //Debug.Log("Mouse down");

            if (Physics.Raycast(ray, out hit, 100.0f))
            {
                //Debug.Log("raycast");

                ray = Camera.main.ScreenPointToRay(Input.mousePosition);
                obj = hit.transform.gameObject;
                Debug.Log(obj + " " + hit.point + obj.GetComponent<Renderer>().material.color);

                if (obj.GetComponent<Renderer>().material.color == Color.green)
                    obj.GetComponent<Renderer>().material.color = Color.white;
                else
                    obj.GetComponent<Renderer>().material.color = Color.green;
                //changeColor();
            }


        }

    }
    public void changeColor()
    {
        
            //string name = hit.transform.name;

            Debug.Log("Point " + hit.point + " is " + hit.transform.name);


            obj = hit.transform.gameObject;
            Debug.Log(obj + " " + hit.point);

            if (obj.GetComponent<Renderer>().material.color == Color.red)
                obj.GetComponent<Renderer>().material.color = Color.white;
            else
                obj.GetComponent<Renderer>().material.color = Color.red;
            //m_Material.color = Color.red;
            // obj.GetComponent<Renderer>().material.color = Color.red;

     
    }
  
}