<div class="Form">
      <div class="property_felters">
        {% comment %}
        <div class="operation_Type" id="sell3_operation_type">
          <p>I want to</p>
          <label class="radio_button"
            >Sell
            <input type="radio" checked="checked" name="sell" />
            <span class="checkmark"></span>
          </label>
          <label class="radio_button"
            >Rental
            <input type="radio" name="rental" />
            <span class="checkmark"></span>
          </label>
        </div>
        {% endcomment %}
        <div class="Select_boxes">
          <div class="sell_3_input">
            <p>Location</p>
            <input
              type="url"
              list="sell-city-input"
              placeholder="put loaction url"
              name="location"
            />
            {% comment %}
            <datalist id="sell-city-input">
              <option value="6 October"></option>
              <option value="Alexandria"></option>
              <option value="Qalyubia"></option>
            </datalist>
            {% endcomment %}
          </div>
          <div class="sell_3_input">
            <p>City</p>
            <input
              type="list"
              list="sell-district-input"
              placeholder="Select"
              name="city"
            />
            <datalist id="sell-district-input">
              <option value="Cairo"></option>
              <option value="Giza"></option>
            </datalist>
          </div>
          <div class="sell_3_input">
            <p>property type</p>
            <input
              type="list"
              list="sell-property-input"
              placeholder="Select"
              name="property type"
            />
            <datalist id="sell-property-input">
              <option value="Villa"></option>
              <option value="Duplex"></option>
              <option value="Apartment"></option>
            </datalist>
          </div>
        </div>
      </div>
      <div class="property_pic">
        <p class="property_headding">Photos for your property</p>
        <div class="pic_vid_container">
          <img src="{%static 'assets/img-stack 1.png'%}" />
          <p class="input-img-vid-details">
            Please drag and drop Add 5:10 images
          </p>
          <label
            ><input
              type="file"
              id="img"
              name="img"
              accept="image/*"
              name="img"
            />
            Upload your images
          </label>
        </div>
      </div>
      <div class="property_vid">
        <p class="property_headding">Videos for your property</p>
        <div class="pic_vid_container">
          <img src="{%static 'assets/video-gallery-2 1.png'%}" />
          <p class="input-img-vid-details">
            Please add a video for your entire property
          </p>
          <label>
            <input
              type="file"
              id="img"
              name="img"
              accept="video/*"
              name="video"
            />
            Upload your Videos
          </label>
        </div>
      </div>

      <div class="owner_details">
        {% comment %}
        <div class="details_row">
          <div class="SelectLocation">
            <label>Name</label>
            <input type="text" placeholder="Enter your name" name="name" />
          </div>
          <div class="SelectLocation">
            <label>Mobile number</label>
            <input
              type="password"
              placeholder="+20 &nbsp;&nbsp;&nbsp;Enter your number"
              name="name"
            />
          </div>
        </div>
        {% endcomment %}
        <div class="details_coloumn">
          <p>
            We will call you in 2 days so we can fill out the rest of
            information and recommend it to our user
          </p>

          <button type="submit"><a href="{%url 'sell4'%}">Send</a></button>
        </div>
      </div>
    </div>